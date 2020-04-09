jQuery(document).ready(function(){
	jQuery('.prop_menu li').on('click', function(){
		jQuery('.prop_menu_active').removeClass('prop_menu_active');
		jQuery(this).addClass('prop_menu_active');
		let cl = `.${jQuery(this).attr('id')}`;
		jQuery('.prop_block').fadeOut(0);
		jQuery(cl).fadeIn();
	});
});