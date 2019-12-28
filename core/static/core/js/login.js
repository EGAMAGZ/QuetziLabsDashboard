var forms=document.getElementsByClassName("form-group");
var next_btn=document.getElementById('next-btn');

var input_email=document.getElementById("id_ad_email");

var errors_email=document.getElementById("id_ad_email_errors");

next_btn.onclick=function(){
    let email=input_email.value;
    if(validateEmail(email)){
        forms[0].style.display="none";
        forms[1].style.display="block";
    }else{
        errors_email.innerHTML='<h6>Error en valores introducidos:</h6><ul class="errorlist"><li>Enter a valid email address.</li></ul>';
    }
};

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}