function getdiagnosis(str) {


    if (/\S/.test(str) && str.length > 1) {
        $.ajax({
            url: "http://127.0.0.1:8000/clinic/api/v1/icd10/",
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
    var str = $(that).parent().children().first().text()
    $(that).parent().remove()
    $("#diagnosis").val(existingStr.replace(str, ""))

}

function openPrevVisits() {
    $('#prevVisits').show('slow')
    $.ajax({
        url: "http://127.0.0.1:8000/clinic/api/v1/icd10/",
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

function populatePrevVisit(uuid, triage_id) {
    $('#print_report').attr('onclick', 'printReport("' + uuid + '")')
    $.ajax({

        url: "http://127.0.0.1:8000/clinic/api/v1/patientvisit/" + uuid,
        type: "get",

        success: function (visit) {


            if (visit.length != 0) {
                $("#prev_diagnosis").text(visit.diagnosis)
                $("#prev_date").text(moment(visit.created))
                $.ajax({
                    url: "http://127.0.0.1:8000/medication/api/v1/models/",
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
                    url: "http://127.0.0.1:8000/nurse/api/v1/models/" + triage_id,
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
    printWindow = window.open("http://127.0.0.1:8000/clinic/clinic_report/" + visit_id + "/");

}

var countyjson = $.getJSON('http://127.0.0.1:8000/static/js/counties.json')


$.each(countyjson, function (i, county) {
    // console.log(county)

})


function dynamic_children() {
    $(function () {
        var no = $('#number_children').val()

        $('#children_td_table').children().remove();

        for (var i = 0; i < no && i < 5; i++) {
            $('#children_td_table')
                .append($('<tr>')
                    .append($('<td>')
                        .append($('<input>')
                            .addClass('Input-text')
                            .attr('name', 'child_name_' + i)))
                    .append($('</td>'))
                    .append($('<td>')
                        .append($('<input>')
                            .addClass('Input-text')
                            .attr('name', 'child_dob_' + i)))
                    .append($('</td>'))
                )
                .append($('</tr>'))

            $("#delete_row").click(function () {
                if (i > 1) {
                    $("#addr" + (i - 1)).html('');
                    i--;
                }
            });
        }
    })
}


