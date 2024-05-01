function validate_form(){
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    email = document.getElementById('email').value
    phone_number = document.getElementById('phone_number').value

    function validateEmail() {
        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    if (!validateEmail(email)) {
        return false;
    }

    if (first_name === '' || last_name ==='' || phone_number === '' || email === '') {
        false
    }
    return true
}

function open_error(message){
    document.getElementById('error_tag').textContent = message
    document.getElementById('error_box').style.display='flex'
}

function sign_up(){
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    email = document.getElementById('email').value
    phone_number = document.getElementById('phone_number').value
    register_as = $("#register_as option:selected").val()
    faculty = $("#faculty option:selected").val()
    department = document.getElementById('department').value


    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    url = window.location.href

    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone_number': phone_number,
        'registered_as': register_as,
        'faculty': faculty,
        'department': department
    }

    function run_request(){
        $.ajax(
            {
                type: 'POST',
                url: url,
                headers: {"X-CSRFToken":csrftoken},
                data: data,
                success: function(responce){
                    if (responce['message']){
                        document.getElementById('main_btn').style.display = 'block'
                        document.getElementById('loader_btn').style.display = 'none'

                        if (responce['status']=='fail'){
                            open_error(responce['message'])
                        }
                        if (responce['status']=='success'){
                            document.getElementById('error_titile').textContent = 'Registeration Successfull'
                            open_error(responce['message'])
                        }
                    }
                },
                error: function(xhr, status, error){
                    document.getElementById('main_btn').style.display = 'block'
                    document.getElementById('loader_btn').style.display = 'none'
                    open_error(error)
                }
            }
        )
    }

    if (validate_form()==true){
        document.getElementById('main_btn').style.display = 'none'
        document.getElementById('loader_btn').style.display = 'flex'

        setTimeout(run_request, 2000);
        
    }else{
        message = 'Check your input fields and try again'
        open_error(message)
    }
}

function closePopup(){
    document.getElementById('error_box').style.display='none'
}