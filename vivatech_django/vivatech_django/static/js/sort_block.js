jQuery(document).ready(function(){

	jQuery('.current_sort').on('click', function(){
		jQuery('.sorts').toggleClass('sorts_open');
		jQuery('.current_sort i').toggleClass('rotate_arrow');
	})
});