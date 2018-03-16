function getdiagnosis(str) {


    if (/\S/.test(str) && str.length > 1) {
        $.ajax({
            url: "/clinic/api/v1/icd10/",
            type: "get",
            data: {
                search: str,
            },
            success: function (json) {
                // console.log(json)
                if (json.length === 0) {
                    $("#no_result").show()
                    $('#searchresult').hide()

                } else {

                    $("#no_result").hide()
                    $('#searchresult').show()
                    $('#search_table tbody').children().remove();
                    var tbody = $('#search_table tbody'),
                        props = ["name", "code"]
                    $.each(json, function (i, diagn) {
                        var tr = $("<tr onclick='addDiag(this)'>");
                        $.each(props, function (i, prop) {
                            $('<td class="mdl-data-table__cell--non-numeric">').html(diagn[prop]).appendTo(tr);
                        });
                        tbody.append(tr);
                    });

                }

            }

        })
    } else {

        $("#no_result").hide()
        $('#searchresult').hide()

    }
}

function addDiag(that) {
    selectedStr = $(that).children().first().text()
    existingStr = $("#diagnosis").val()
    if (existingStr.length > 0) {
        $("#diagnosis").val(existingStr + ", " + selectedStr + "~" + $(that).children().first().next().text())
        $("#diag_search").val('')
        tagify(selectedStr)


    } else {
        $("#diagnosis").val(selectedStr + "~" + $(that).children().first().next().text())
        $("#diag_search").val('')
        tagify(selectedStr)

    }
}

function tagify(selectedStr) {
    $("#diag_sect").append(
        $('<span/>')
            .attr("id", selectedStr.split(' ').join('_'))
            .addClass("mdl-chip mdl-chip--deletable")
            .append(
                $('<span/>')
                    .addClass("mdl-chip__text")
                    .append("<span/>")
                    .text(selectedStr)
            )
            .append(
                $('<button/>').addClass('mdl-chip__action')
                    .prop('type', 'button')
                    .append(
                        $('<i/>')
                            .addClass('material-icons')
                            .text('cancel')
                    )
                    .attr('onclick', 'removeDiag(this)')
            )
    )
    $("#searchresult").hide()

}

function removeDiag(that) {
    //get the string in the tag and remove trailing whitespaces
    var str = $(that).parent().children().first().text().trim()

    //remove tag
    $(that).parent().remove()

    //get the current diagnosis string
    var existingStr = $("#diagnosis").val()

    //remove the deleted text from the hidden diagnosis text area box
    $("#diagnosis").val(existingStr.replace(str, ""))

    //remove trailing commas after spliting diagnosis
    $("#diagnosis").val($("#diagnosis").val().replace(/(^,)|(,$)/g, ""))

}

function openPrevVisits() {
    $('#prevVisits').show('slow')
    $.ajax({
        url: "/clinic/api/v1/icd10/",
        type: "get",

        success: function (json) {
            // console.log(json)
            if (json.length === 0) {
                $("#no_result").show()
                $('#searchresult').hide()

            } else {

                $("#no_result").hide()
                $('#searchresult').show()
                var tbody = $('#search_table tbody'),
                    props = ["name", "code"]
                $.each(json, function (i, diagn) {
                    var tr = $("<tr onclick='addDiag(this)'>");
                    $.each(props, function (i, prop) {
                        $('<td class="mdl-data-table__cell--non-numeric">').html(diagn[prop]).appendTo(tr);
                    });
                    tbody.append(tr);
                });

            }

        }

    })

}

function closePrevVisits() {
    $('#prevVisits').hide('slow')

}

//uuid is the visit id used to get the previous visit via url
//the triage id is the patient's session id during a treatment session
function populatePrevVisit(uuid, triage_id) {
    console.log("the visit_id id is: " + uuid)
    console.log("the triage_id id is: " + triage_id)
    $('#print_report').attr('onclick', 'printReport("' + uuid + '")')
    $.ajax({

        url: "/clinic/api/v1/patientvisit/" + uuid,
        type: "get",

        success: function (visit) {
            console.log(visit)
            if (visit.length != 0) {
                $("#prev_diagnosis").text(visit.diagnosis)
                $("#prev_summary").text(visit.plan_of_managemnt)
                $("#prev_date").text(moment(visit.created))
                $("#prev_doc_notes").text(visit.notes)
                $("#prev_his_illness").text(visit.his_presenting_illness)
                $("#prev_examination").text(visit.examination)
                $("#prev_query_diag").text(visit.query_diagnosis)
                $.ajax({
                    url: "/medication/api/v1/models/",
                    type: "get",
                    data: {
                        search: visit.triage_id
                    },

                    success: function (prescription) {
                        // console.log(prescription

                        if (prescription.length != 0) {
                            $("#prev_prescription").text(prescription.prescription)

                        } else {
                            $("#prev_prescription").text("No prescription Found")

                        }

                    }

                })

                $.ajax({
                    url: "/nurse/api/v1/models/" + triage_id,
                    type: "get",

                    success: function (triage) {
                        // console.log(triage)
                        if (triage.length != 0) {
                            $("#prev_bp").text(triage.systolic + "/" + triage.diastolic)
                            $("#prev_random_glucose").text(triage.random_glucose)
                            $("#prev_temp").text(triage.temperature)
                            $("#prev_heart_rate").text(triage.heart_rate)
                            $("#prev_weight").text(triage.weight)
                            $("#prev_height").text(triage.height)
                            $("#prev_oxygen").text(triage.oxygen_saturation)
                            $("#prev_urinalysis").text(triage.urinalysis)
                            $("#prev_other").text(triage.others)


                        } else {

                        }

                    }

                });

                openPrevVisits()


            } else {


            }

        }

    })
}

function saveDiagnosis() {
    console.log($('#clinicPrescriptionForm').serialize())

    var prescription_url = "/medication/models/new/" + $('#pres_id_patient_no').val() + "/";
    var clinic_url = "/clinic/patientvisit/doctor/" + $('#pres_id_patient_no').val() + "/";

    var formdata = {
        'patient_no': $('input[name=pres_patient_no]').val(),
        'patient_name': $("#first_name").val() + " " + $("#last_name").val(),
        'email': $('input[name=pres_email]').val(),
        'phone_number': $('input[name=pres_phone_number]').val(),
        'address': $('#pres_id_address').val(),
        'prescription': $('#pres_prescription').val(),
    };

}

function savePrescription() {
    $.ajax({
        type: "POST",
        url: clinic_url,
        data: $('#visit').serialize(),
        datatype: 'json',
        xhrFields: {
            withCredentials: true
        },
        success: function (data) {
            $.ajax({
                type: "POST",
                url: prescription_url,
                data: $('#clinicPrescriptionForm').serialize(),
                datatype: 'json',
                xhrFields: {
                    withCredentials: true
                },
                success: function (data) {
                    alert("Succesfully");
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    alert(textStatus, errorThrown, "Could not Submit Prescription");
                },
            });

            $('#prescription_form_').attr('disabled', 'true')

            window.location = "/clinic/patientvisit/create/"
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert(textStatus, errorThrown);
        },
    });
}


$('#clinicPrescriptionForm').on('submit', function (event) {
    event.preventDefault();
    console.log("form submitted!") // sanity check
    savePrescription();
});

function close_Modal(id_name) {
    $('#' + id_name).hide('slow')
}

function successPopUp() {
    if (!$('.dialog').showModal) {
        dialogPolyfill.registerDialog(dialog);
    }
    $('.dialog').showModal();
}

function closePopUp() {
    $('.dialog').close();
}

function show_element(id_name) {
    $('#' + id_name).show()
}

function hide_element(id_name) {
    $('#' + id_name).hide()
}


function showTest(sender) {

    if (sender === "tests_radiology") {
        $('#' + "tests_labs").hide()
        $('#' + "tests_radiology").show()
        $('#' + 'test_results').show('slow')
    } else {
        $('#' + "tests_labs").show()
        $('#' + "tests_radiology").hide()
        $('#' + 'test_results').show('slow')

    }

}

function printReport(visit_id) {
    printWindow = window.open("/clinic/clinic_report/" + visit_id + "/");

}

var countyjson = $.getJSON('/static/js/counties.json')


$.each(countyjson, function (i, county) {
    // console.log(county)

})

$(function () {
    dynamic_children()
    console.log("Finished")
});

function dynamic_children() {
    $(function () {
        var no = $('#number_children').val()
        $('#id_children-TOTAL_FORMS').val = no

        children_added = $('#children_td_table tr').length
        remaining = 4 - children_added

        //determine if the no of children input are more than those left
        if (no > remaining) {
            //show alert that max children reached
            $('max-children').show()
            setTimeout(function () {
                $('max-children').hide()
            }, 3000);
        } else if(no<children_added){

            no_to_remove = children_added-no
            for (i=0; i<no_to_remove; i++){
                $('#children_td_table').children().last().remove();
            }

        }
        else {
            for (var i = 0; i < remaining && i < no; i++) {
                no_ = i + 1
                $('#children_td_table')
                    .append($('<tr>')
                        .append('<td>' + no_ + '</td>')
                        .append($('<td>')
                            .append($('<input>')
                                .addClass('Input-text')
                                .attr('name', 'children-' + i + '-child_name')))
                        .append($('</td>'))
                        .append($('<td>')
                            .append($('<input>')
                                .addClass('Input-text')
                                .attr('name', 'children-' + i + '-child_dob')
                                .prop('type', 'date')
                                .prop('class', 'children-' + i + '-child_age')
                                .change(function () {
                                    d = new Date($(this).val());
                                    var before = moment($(d, 'YYYY-MM-DD'));
                                    var age = moment().diff(d, 'years');
                                    age_id_name = "#" + $(this).attr('class')
                                    $(age_id_name).val(age);
                                })
                            ))
                        .append($('</td>'))
                        .append($('<td>')
                            .append($('<input>')
                                .addClass('Input-text')
                                .attr('id', 'children-' + i + '-child_age')
                                .attr('name', 'child')
                                .prop('type', 'text')
                            ))
                        .append($('</td>'))
                    )
                    .append($('</tr>'))
            }

        }


        //
        // for (var i = 0; i < no && i < 4; i++) {
        //
        //
        //     $("#delete_row").click(function () {
        //         if (i > 1) {
        //             $("#addr" + (i - 1)).html('');
        //             i--;
        //         }
        //     });
        // }
    })
}

function csrfSetUP() {
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    csrftoken = $('input[name="csrfmiddlewaretoken"]').attr('value')

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

}
function closepatientscase(patient_id) {
    csrfSetUP()

    console.log($('#visit').serialize())

    $.ajax({
        url: "/clinic/patientvisit/doctor/" + patient_id + "/",
        type: "POST",
        datatype: 'json',
        data: $('#visit').serialize(),
        xhrFields: {
            withCredentials: true
        },
        success: function (json) {
            $.ajax({
                url: "/clinic/patientvisit/close/" + patient_id + "/",
                type: "get",
                success: function (json) {
                    window.location.href = "/clinic/patientvisit/create/"
                },
                failure: function (json) {
                    alert("Something Went wrong. Try again.")
                }

            });
        }

    });

}

function genericTagify(selectedStr, divid, div_to_remove) {
    $("#" + divid).append(
        $('<span/>')
            .attr("id", selectedStr.split(' ').join('_'))
            .addClass("mdl-chip mdl-chip--deletable")
            .append(
                $('<span/>')
                    .addClass("mdl-chip__text")
                    .append("<span/>")
                    .text(selectedStr)
            )
            .append(
                $('<button/>').addClass('mdl-chip__action')
                    .prop('type', 'button')
                    .append(
                        $('<i/>')
                            .addClass('material-icons')
                            .text('cancel')
                    )
                    .attr('onclick', 'genericRemoveDiag(this,' + div_to_remove + ')')
            )
    )
    // $("#searchresult").hide()

}

function genericRemoveDiag(that, div_to_remove) {
    //get the string in the tag and remove trailing whitespaces
    var str = $(that).parent().children().first().text().trim()


    //remove tag
    $(that).parent().remove()
    console.log('')

    //get the current diagnosis string
    var existingStr = $("#id_prescription").val()

    //remove the deleted text from the hidden diagnosis text area box
    $("#id_prescription").val(existingStr.replace(str, ""))

    //remove trailing commas after spliting diagnosis
    $("#id_prescription").val($("#id_prescription").val().replace(/(^,)|(,$)/g, ""))

}


function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    var row = $('.dynamic-form:first').clone(true).get(0);
    $(row).removeAttr('id').insertAfter($('.dynamic-form:last')).children('.hidden').removeClass('hidden');
    $(row).children().not(':last').children().each(function () {
        updateElementIndex(this, prefix, formCount);
        $(this).val('');
    });
    $(row).find('.delete-row').click(function () {
        deleteForm(this, prefix);
    });
    $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
    return false;
}

function deleteForm(btn, prefix) {
    $(btn).parents('.dynamic-form').remove();
    var forms = $('.dynamic-form');
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
        $(forms.get(i)).children().not(':last').children().each(function () {
            updateElementIndex(this, prefix, i);
        });
    }
    return false;
}