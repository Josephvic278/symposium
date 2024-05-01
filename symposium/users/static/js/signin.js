function validate_form(){
    email = document.getElementById('email').value
    phone_number = document.getElementById('phone_number').value

    function validateEmail() {
        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    if (!validateEmail(email)) {
        return false;
    }

    if ( phone_number === '' || email === '') {
        false
    }
    return true
}

function open_error(message){
    document.getElementById('error_tag').textContent = message
    document.getElementById('error_box').style.display='flex'
}

function sign_in(){
    email = document.getElementById('email').value
    phone_number = document.getElementById('phone_number').value

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    url = window.location.href

    data = {
        'email': email,
        'phone_number': phone_number
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
                            document.getElementById('db_download').style.display = 'none'
                        }
                        if (responce['status']=='success'){
                            document.getElementById('error_titile').textContent = 'Admin login Successfull'
                            open_error(responce['message'])
                            document.getElementById('db_download').style.display = 'block'
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
    document.getElementById('database').style.display = 'block'
    document.getElementById('error_box').style.display='none'
}