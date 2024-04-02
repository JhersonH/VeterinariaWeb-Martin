$("#crear-cuenta").on("click", function(){
    $("#myModal").modal('hide');
    $("#myModal1").modal('show')
})

$('#myModal').on('hidden.bs.modal', function() {
    $('#femail').trigger('focus');
    $('#formLogin')[0].reset();
});

$('#myModal1').on('hidden.bs.modal', function() {
    $('#email').trigger('focus');
    $('#formRegistro')[0].reset();
});

$('#myModal1').on('shown.bs.modal', function() {
    $('#nombre').trigger('focus');
});

$('#myModal3').on('hidden.bs.modal', function() {
    $('#email').trigger('focus');
    $('#formContacto')[0].reset();
});

$('#myModal3').on('shown.bs.modal', function() {
    $('#fname').trigger('focus');
});