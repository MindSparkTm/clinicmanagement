//customized from http://knockoutjs.com/examples/contactsEditor.html
var initialData = [
    {
        number_children: "1", children: []
    },

];

var IfChildrenModel = function (if_children) {
    var self = this;
    self.if_children = ko.observableArray(ko.utils.arrayMap(if_children, function (child) {
        return {number_children: child.number_children, children: ko.observableArray(child.children)};
    }));

    self.addContact = function () {
        self.if_children.push({
            number_children: "",
            children: ko.observableArray()
        });
    };

    self.removeContact = function (contact) {
        self.if_children.remove(contact);
    };

    self.addChild = function (contact) {
        contact.children.push({
            name: "",
            age: ""
        });
    };

    self.removeChild = function (child) {
        $.each(self.if_children(), function () {
            this.children.remove(child)
        })
    };

    // self.save = function() {
    //     self.lastSavedJson(JSON.stringify(ko.toJS(self.if_children), null, 2));
    // };
    //
    // self.lastSavedJson = ko.observable("")
};

ko.applyBindings(new IfChildrenModel(initialData));


function getdiagnosis(str) {
    $('#search_table tbody').children().remove();

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
                    var tbody = $('#search_table tbody'), props = ["name", "code"]
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
    if (existingStr.length>0){
        $("#diagnosis").val(existingStr+", "+selectedStr+"~"+$(that).children().first().next().text())
        $("#diag_search").val('')
        tagify(selectedStr)


    } else {
        $("#diagnosis").val(selectedStr+"~"+$(that).children().first().next().text())
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

function removeDiag(that){
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
                    var tbody = $('#search_table tbody'), props = ["name", "code"]
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

function populatePrevVisit(uuid){
    $.ajax({
            url: "http://127.0.0.1:8000/clinic/api/v1/patientvisit/"+uuid,
            type: "get",

            success: function (visit) {
                if (visit.length != 0) {
                    $("#prev_diagnosis").text(visit.diagnosis)
                    $("#prev_date").text(moment(visit.created))
                    $.ajax({
                        url: "http://127.0.0.1:8000/medication/api/v1/models/" + visit.prescription_id,
                        type: "get",

                        success: function (prescription) {
                            // console.log(prescription)
                            if (prescription.length != 0) {
                                $("#prev_prescription").text(prescription.prescription)

                            } else {
                                $("#prev_prescription").text("No prescription Found")

                            }

                        }

                    })
                    $.ajax({
                        url: "http://127.0.0.1:8000/nurse/api/v1/models/" + visit.triage_id,
                        type: "get",

                        success: function (triage) {
                            // console.log(triage)
                            if (triage.length != 0) {
                                $("#prev_bp").text(triage.systolic+ "/" + triage.diastolic)
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

function postPrescription(){
    console.log($('#clinicPrescriptionForm').serialize())

    var url = "/medication/models/new/"+$('input[name=pres_patient_no]').val()+"/";
    var clinic_url = "/clinic/patientvisit/doctor/"+$('input[name=pres_patient_no]').val()+"/";

    var formdata = {
            'patient_no': $('input[name=pres_patient_no]').val(),
            'patient_name': $("#first_name").val()+" "+$("#last_name").val(),
            'email': $('input[name=pres_email]').val(),
            'phone_number': $('input[name=pres_phone_number]').val(),
            'address': $('#pres_id_address').val(),
            'prescription': $('#pres_prescription').val(),
        };
    $.ajax({
        type: "POST",
        url: clinic_url,
        data: $('#visit').serialize(),
        datatype: 'json',
        xhrFields: {
            withCredentials: true
        },
           success: function(data)
           {
               $.ajax({
                   type: "POST",
                   url: url,
                   data: $('#clinicPrescriptionForm').serialize(),
                   datatype: 'json',
                   xhrFields: {
                       withCredentials: true
                   },
                   success: function (data) {
                   },
                   error: function (jqXHR, textStatus, errorThrown) {
                       alert(textStatus, errorThrown);
                   },
               });

               $('#prescription_form_').attr('disabled','true')
               alert("Succesful");
               window.location="/clinic/patientvisit/create/"
           },
        error: function(jqXHR, textStatus, errorThrown)
           {
               alert(textStatus, errorThrown);
           },
         });


}


// Submit post on submit
$('#clinicPrescriptionForm').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    postPrescription();
});

function close_Modal(id_name){
    $('#'+id_name).hide('slow')
}

function successPopUp(){
    if (! $('.dialog').showModal) {
      dialogPolyfill.registerDialog(dialog);
    }
    $('.dialog').showModal();
}
function closePopUp(){
    $('.dialog').close();
}

function showTest(triage_no){
    $.ajax({
        url: "http://127.0.0.1:8000/labs/api/v1/tests/" + visit.triage_id,
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

    })
}