/* 
$(document).ready(function() {
	$('.bxslider').bxSlider();
	
	$(".menu-trigger").click(function() {
		$("#menu").fadeToggle(300);
		$(this).toggleClass("active")
	});
	
	$('.info-request, .get-contact').fancybox();
	
	$("select").crfs(); 
	
	
	$(".table td").mouseenter(function(){    
        $(this).find(".holder").stop(true, true).fadeIn(600);
        $(this).find(">div").addClass('hover');
        return false;
     });
      $('.table td').mouseleave(function(){  
        $(this).find(".holder").stop(true, true).fadeOut(400);
        $(this).find(">div").removeClass('hover');
        return false;
     });
	$(".table td .holder").click(function() {
        $(this).stop(true, true).fadeOut(400);
        $(this).parent().parent().removeClass('hover');
        return false;
	});
	
	var isBrowserOs = {
	    Windows: function() {
	        return navigator.userAgent.match(/Win/i);
	    },
	    MacOS: function() {
	        return navigator.userAgent.match(/Mac/i);
	    },
	    UNIX: function() {
	        return navigator.userAgent.match(/X11/i);
	    },
	    Linux: function() {
	        return navigator.userAgent.match(/Linux/i);
	    },
	    iOs: function() {
	        return navigator.userAgent.match(/(iPad|iPhone|iPod)/i);
	    },
	    Android: function() {
	        return navigator.userAgent.match(/android/i);
	    },
	    BlackBerry: function() {
	        return navigator.userAgent.match(/BlackBerry/i);
	    },
	    Chrome: function() {
	        return window.chrome;
	    },
	    Firefox: function() {
	        return navigator.userAgent.match(/Firefox/i);
	    },
	    IE: function() {
	        return navigator.userAgent.match(/MSIE/i);
	    },
	    Opera: function() {
	        return (!!window.opera || navigator.userAgent.indexOf(' OPR/') >= 0);
	    },
	    SeaMonkey: function() {
	        return navigator.userAgent.match(/SeaMonkey/i);
	    },
	    Camino: function() {
	        return navigator.userAgent.match(/Camino/i);
	    },
	    Safari: function() {
	        return (Object.prototype.toString.call(window.HTMLElement).indexOf('Constructor') > 0);
	    }
	};
	 
	var html_class = '';
	//OS
	if(isBrowserOs.Windows())
		html_class = 'win';
	if(isBrowserOs.UNIX())
		html_class = 'unix';
	if(isBrowserOs.MacOS())
		html_class = 'mac';
	if(isBrowserOs.Linux())
		html_class = 'linux';
	if(isBrowserOs.iOs())
		html_class = 'ios mac';
	if(isBrowserOs.Android())
		html_class = 'android';
	if(isBrowserOs.BlackBerry())
		html_class = 'blackberry';
	 
	//Browser
	if(isBrowserOs.Chrome())
		html_class = html_class + ' chrome';
	if(isBrowserOs.Firefox())
		html_class = html_class + ' firefox';
	if(isBrowserOs.IE())
		html_class = html_class + ' ie';
	if(isBrowserOs.Opera())
		html_class = html_class + ' opera';
	if(isBrowserOs.SeaMonkey())
		html_class = html_class + ' seamonkey';
	if(isBrowserOs.Camino())
		html_class = html_class + ' camino';
	if(isBrowserOs.Safari())
		html_class = html_class + ' safari';
	 
	$("html").addClass(html_class);
	 
});


*/

(function ($) {
    "use strict";


    /*==================================================================
    [ Focus input ]*/
    $('.input100').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })
    })


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }

    /*==================================================================
    [ Show pass ]*/
    var showPass = 0;
    $('.btn-show-pass').on('click', function(){
        if(showPass == 0) {
            $(this).next('input').attr('type','text');
            $(this).find('i').removeClass('zmdi-eye');
            $(this).find('i').addClass('zmdi-eye-off');
            showPass = 1;
        }
        else {
            $(this).next('input').attr('type','password');
            $(this).find('i').addClass('zmdi-eye');
            $(this).find('i').removeClass('zmdi-eye-off');
            showPass = 0;
        }

    });


})(jQuery);
