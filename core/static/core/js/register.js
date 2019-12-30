var input_img=document.getElementById('id_ad_profile');
var profile_img=document.getElementById('profile-img');

input_img.onchange=function (evt) {
    var tgt = evt.target || window.event.srcElement,
        files = tgt.files;
// console.log(files[0].name);

    // FileReader support
    if (FileReader && files && files.length) {
        let file_name=files[0].name;
        if(validate_fileupload(file_name)){
            var fr = new FileReader();
            fr.onload = function () {
                profile_img.src = fr.result;
            }
            fr.readAsDataURL(files[0]);
        }else{
            alert("Archivo No Soportado");
        }
    }

    // Not supported
    else {
        // fallback -- perhaps submit the input to an iframe and temporarily store
        // them on the server until the user's session ends.
    }
}

function validate_fileupload(fileName)
{
    var allowed_extensions = new Array("jpg","png","gif");
    var file_extension = fileName.split('.').pop().toLowerCase(); // split function will split the filename by dot(.), and pop function will pop the last element from the array which will give you the extension as well. If there will be no extension then it will return the filename.

    for(var i = 0; i <= allowed_extensions.length; i++)
    {
        if(allowed_extensions[i]==file_extension)
        {
            return true; // valid file extension
        }
    }

    return false;
}