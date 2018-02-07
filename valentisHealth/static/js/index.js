
//customized from http://knockoutjs.com/examples/contactsEditor.html
var initialData = [
    { number_children: "1", children: [
        ]
    },

];

var IfChildrenModel = function(if_children) {
    var self = this;
    self.if_children = ko.observableArray(ko.utils.arrayMap(if_children, function(child) {
        return { number_children: child.number_children, children: ko.observableArray(child.children) };
    }));

    self.addContact = function() {
        self.if_children.push({
            number_children: "",
            children: ko.observableArray()
        });
    };

    self.removeContact = function(contact) {
        self.if_children.remove(contact);
    };

    self.addChild = function(contact) {
        contact.children.push({
            name: "",
            age: ""
        });
    };

    self.removeChild = function(child) {
        $.each(self.if_children(), function() { this.children.remove(child) })
    };

    // self.save = function() {
    //     self.lastSavedJson(JSON.stringify(ko.toJS(self.if_children), null, 2));
    // };
    //
    // self.lastSavedJson = ko.observable("")
};

ko.applyBindings(new IfChildrenModel(initialData));

