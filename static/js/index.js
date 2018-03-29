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
        } else if (no < children_added) {

            no_to_remove = children_added - no
            for (i = 0; i < no_to_remove; i++) {
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


function calculateAge(dateString) {
    var today = new Date();
    var birthDate = new Date(dateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return (age < 0 || isNaN(age)) ? 0 : age;
}

function setDob(birthday) {
    age = calculateAge(birthday)
    console.log(age, " is the age for ", birthday)
    $('#textfield_age').val(age)
}


$(function () {
    var dtToday = new Date();

    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();

    if (month < 10)
        month = '0' + month.toString();
    if (day < 10)
        day = '0' + day.toString();

    var maxDate = year + '-' + month + '-' + day;
    $('input[type="date"]').attr('max', maxDate);
});

function readonly_personal() {
    $("#personal_information :input").attr("readonly", true);
}


// ###################################Prescription form handling################################


var brand = [];
var data = [];
var results = [];
var s;
var clicked = 0;
var sr = "";

$(window).on("load", getdata());
var patient_id = $("#id_patient_no").val();

var tablets = '--'
var days = '--'
var freq = '--'


//update the search result list function
function getsearch(str) {
    drugs = brand

    if (/\S/.test(str) && str.length > 1) {
        var options = {
            keys: ['brand'],
        }
        var fuse = new Fuse(drugs, options)

        //fuse to do the text search on the array
        json = fuse.search(str)

        //if there are not result show "no result" message
        if (json.length === 0) {
            $("#no_result").show()
            $('#searchresult').hide()

        } else {
            console.log(json, drugs)
            $("#no_result").hide()
            $('#searchresult').show()

            //remove existing search result
            $('#search_table tbody').children().remove();
            var tbody = $('#search_table tbody'),
                brand_key = "brand"
            $.each(json, function (i, brand_key) {

                var tr = $("<tr>");
                //append new results to the search result list
                $('<td class="mdl-data-table__cell--non-numeric">').html(brand[brand_key]).appendTo(tr);
                tbody.append(tr);
            });

        }
    } else {

        $("#no_result").hide()
        $('#searchresult').hide()

    }
}

///here we create a pop up to allow the specifying of the dosage
$(function () {
    $('#livesearch').on('click', 'td', function () {
        that = this

        var dialog = bootbox.dialog({
            title: 'Dosage for ' + $(this).text(),
            message: "<input onkeyup='tablets=$(this).val()' class='form-control' id='tablets' placeholder='No of Tablets/ML'><br><input  onkeyup='freq=$(this).val()' class='form-control' id='freq' placeholder='No of time per day'><br><input onkeyup='days=$(this).val()' class='form-control' id='days' placeholder='No of Days'>",
            buttons: {
                cancel: {
                    label: "cancel",
                    className: 'btn-danger',
                    callback: function () {

                    }
                },

                ok: {
                    label: "ok",
                    className: 'btn-info',
                    callback: function () {

                        console.log("sr", sr);


                        var dosage = '(tablets:' + tablets + ' ' + ' times per day:' + freq + ' ' + 'days:' + days + ')'

                        sr = sr + $(that).text() + ' ' + dosage + "\n";
                        genericTagify($(that).text() + ' ' + dosage, 'prescription_tags', 'id_prescription')

                        $('#id_prescription').val(sr)

                        tablets = '--'
                        days = '--'
                        freq = '--'


                    }
                }
            }
        });


    });


    //Handle email button clicked
    $("#sendemail").click(function (e) {

        id_patient_no
        id_patient_name
        textfield_phone_number
        textfield_email
        id_address
        id_prescription
        var patientnumber = $("#id_patient_no").val();
        var patientname = $("#id_patient_name").val();
        var phonenumber = $("#textfield_phone_number").val();
        var email = $("#textfield_email").val();
        var address = $("#id_physical_address").val();
        var prescriptionid = $("#id_prescription").val();

        var prescriptiondata = "patientname" + "  " + patientname + " " + "patientnumber" + " " + patientnumber + "  " +
            "phonenumber" + "  " + phonenumber + "  " + "email" + " " + email + "address" + "  " + address + " " + "prescription" + "  " + prescriptionid;

        sendprescriptionemail("notifications@valentishealth.co.ke", prescriptiondata, "notifications@valentishealth.co.ke")
        sendprescriptionemail("hello@redpulse.co.ke", prescriptiondata, "hello@redpulse.co.ke")
//           sendprescriptionemail("prescription@mydawa.com", prescriptiondata, "notifications@valentishealth.co.ke")


    });

})


var cb = $("input#check");

if (cb.is(":checked")) {
    console.log("checkbox is checked ");
} else {
    console.log("checkbox is not checked");
}

function clearprescriptionarea() {
    $("#clrbtn").val("");
}


//generic emailing function implementation
function sendprescriptionemail(dest_email, prescriptiondata, senderemail) {
    var reqbody = {

        "personalizations": [
            {
                "to": [
                    {
                        "email": dest_email
                    }
                ],
                "subject": prescriptiondata,
            }
        ],
        "from": {
            "email": senderemail
        },
        "content": [
            {
                "type": "text/plain",
                "value": "Prescription"
            }
        ]

    }
    reqbody = JSON.stringify(reqbody);
    // console.log('requestbody', reqbody);


    $.ajax({
            method: 'POST',
            url: "https://cors-anywhere.herokuapp.com/https://api.sendgrid.com/v3/mail/send",
            data: reqbody,
            dataType: 'json',
            headers: {
                'Authorization': 'Bearer ' + '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',
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },

            crossDomain: true,
            success: function (res) {
                alert("email was sent successfully")
                console.log(1, res)
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }

        })
        .done(function (res) {
            alert("email was sent successfully")
            console.log(1, res)
        })
        .fail(function (e) {
            console.log(2, e.status, e.responseText)
        })
}


function getdata() {
    $.ajax({
        url: "/medication/api/v1/MyDawa/",
        type: "GET",
        success: function (response) {
            s = response;
            for (var i = 0; i < response.length; ++i) {

                brand.push(response[i].brand);
            }

            console.log("loaded", patient_id);
            //getprescriptiondata(patient_id);


        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }


    });

}


// ###################################End of rescription form handling################################