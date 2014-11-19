
// var support = ["zh-tw", "en"];
var CURRENT_LANG = "";
var DEFAULT_LANG = "zh";

$(window).on('hashchange', function(e){

	var hash = location.hash;
	var lang = hash.replace( /^#/, '' );

	if(lang) {
		CURRENT_LANG = lang;
	}else {
		CURRENT_LANG = DEFAULT_LANG; // default
	}
	changeLanguage(CURRENT_LANG);
});

function changeLanguage(lang)
{

	// find all tags with attribute "lang"
	$.each( $('*[lang]'), function(i, this_obj){

		// ignore <HTML> and <BODY> tags
		if ( this_obj.tagName.toUpperCase() == "HTML"  || this_obj.tagName.toUpperCase() == "BODY")	{
			return true;
		}

		// get the lang of this obj
		var this_lang = $(this_obj).attr("lang").toLowerCase();

		// amend link if the attr href has been found
		var attr = $(this_obj).attr('href');
		if (typeof attr !== typeof undefined && attr !== false) {
			var current_href = $(this_obj).attr("href");
			if ( current_href.indexOf("#"+this_lang) < 0 ) {
				$(this_obj).attr("href", current_href+"#"+this_lang);	
			}			
		}
		// toggle language
		if ( this_lang != lang )
		{
			if ( !$(this_obj).hasClass("hide") )
			{
				$(this_obj).addClass("hide");
			}			
		}
		else
		{
			$(this_obj).removeClass("hide");
		}
	});
}



$(document).ready(function(){
	// $(window).trigger('hashchange');
})