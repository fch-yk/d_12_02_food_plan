function SetDisabled() {
    document.getElementById('username').disabled=1;
    document.getElementById('password1').disabled=1;
    document.getElementById('password2').disabled=1;
}

function Vanish() {
    document.getElementById('error').style.cssText='opacity: 0; transition: 0.3s';
}

function ChangeUsername() {
    document.getElementById('username').disabled=0;
}   


function ChangePassword() {
    document.getElementById('password1').disabled=0;
    document.getElementById('password2').disabled=0;
}   
window.onload = SetDisabled;