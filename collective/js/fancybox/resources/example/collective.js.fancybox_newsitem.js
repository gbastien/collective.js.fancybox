/*
 * FancyBox - Activates the Fancybox on 'News item' selected image
 */

jQuery(document).ready(function() {
$("a#parent-fieldname-image").fancybox({
'titleShow' : true,
'transitionIn'	:	'elastic',
'transitionOut'	:	'elastic',
'opacity'       :       true,
}); 
})
