function prefill_building_data_update(id) {
    document.getElementById("updateAddressForm").action = "/buildings/update/"+id.querySelector('#id').innerHTML+"/";
    document.getElementById("formUpdateId_span").textContent = id.querySelector('#id').innerHTML;
    document.getElementById("formUpdateCity").value = id.querySelector('#city').innerHTML;
    document.getElementById("formUpdateStreet").value = id.querySelector('#street').innerHTML;
    document.getElementById("formUpdateHouse").value = id.querySelector('#house').innerHTML;
};

function prefill_building_data_delete(id) {
    document.getElementById("submit_delete").href = "/buildings/delete/"+id.querySelector('#id').innerHTML+"/";
};

function prefill_user_data_update(id) {
    document.getElementById("updateUserForm").action = "/users/update/"+id.querySelector('#id').innerHTML+"/";
    document.getElementById("formUpdateId_span").textContent = id.querySelector('#id').innerHTML;
    document.getElementById("formUpdateId").value = id.querySelector('#id').innerHTML;
    document.getElementById("formUpdateName").value = id.querySelector('#name').innerHTML;
    document.getElementById("formUpdateSurname").value = id.querySelector('#surname').innerHTML;
    document.getElementById("formUpdateTelephone").value = id.querySelector('#telephone').innerHTML;
    document.getElementById("formUpdateBuilding").value = id.querySelector('#house').getAttribute('value');
    document.getElementById("formUpdateFlat").value = id.querySelector('#flat').innerHTML;
};

function prefill_profile_data_delete(id) {
    document.getElementById("submit_delete").href = "/users/delete/"+id.querySelector('#id').innerHTML+"/";
};