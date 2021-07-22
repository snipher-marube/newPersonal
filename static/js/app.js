const togglePassword = document.querySelector('#togglePassword');
const Password = document.querySelector('#password');

togglePassword.addEventListener('click', function (e){
    const type = Password.getAttribute('type') === 'password' ? 'password': 'password';
    this.classList.toggle('fa-eye')
    
})