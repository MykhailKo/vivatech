jQuery(document).ready(function(){
	// Language menu switcher
	let lang = localStorage.getItem('lang') != null ? localStorage.getItem('lang') : 'ru';
	jQuery(`#${lang}`).addClass('lang_hide');
	
	jQuery('.lang_menu a').on('click', function(event){
		localStorage.setItem('lang', jQuery(this).attr('id'));
		jQuery('.lang_menu a').toggleClass('lang_hide');	
	});

	//to top button 
	jQuery(document).on('scroll', function(){
		if(jQuery(document).scrollTop() > 400){
			jQuery('.to_top').fadeIn();
		}else {
			jQuery('.to_top').fadeOut();
		}
	});

	jQuery('.to_top').on('click', function(){
		jQuery([document.documentElement, document.body]).animate({
			scrollTop: 0
		}, 500);
		return false;
	});
	//cuurent menu item highlight
	let p_det = false;
	let url = document.location.toString();
	jQuery('.site-navigation li').each(function(i){
		if(url.includes(jQuery(this).children('a').attr('href'))){
			jQuery(this).addClass('current-menu-item');
			p_det = true;
		} else {
			jQuery(this).removeClass('current-menu-item');
		}
	});
		
	/*if(page == "http://example.com"){
		jQuery('#main').parent().children('.btn_hover').attr('id', 'onlink');
	}*/


	//fix header when scrolling 
	jQuery(document).on('scroll', function(){
		let s_top = jQuery(document).scrollTop();
		if(s_top > 50){
			jQuery('.nav-bar').addClass('nav-scrolled');
		}else {
			jQuery('.nav-bar').removeClass('nav-scrolled');
		}
	});
});