jQuery(document).ready(function(){
	jQuery('#send').on('click', function(event){
		if(
			jQuery('#full_name').val() == '' ||
			jQuery('#subject').val() == '' ||
			jQuery('#email').val() == '' ||
			jQuery('#text').val() == '' 
		){
			alert("Заполните все поля формы перед отпрвкой!");
		}else {
			jQuery(this).attr('type', 'submit');
		}
	});
});