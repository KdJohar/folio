$(document).ready(function() {

	/*======= Anchor Tag Text flip Roll Over  =================== */ 

	function linkify(selector) {
		
		var supports3DTransforms = document.body.style['webkitPerspective'] !== undefined || document.body.style['MozPerspective'] !== undefined;
		if (supports3DTransforms) { 
			var nodes = selector;  
			for (var i = 0, len = nodes.length; i < len; i++) {
				var node = nodes[i]; 
				if (!node.className) {
					node.className += ' roll';
					node.innerHTML = '<span data-title="' + node.text + '">' + node.innerHTML + '</span>';
				}
			}
		}
	} 
	
	/* Select all anchor tag except class inside bracket*/ 
	
	linkify($("a:not(.carousel-control,.btn,.dropdown-toggle,.dropdown-menu a,a.no-flip,.no-flip a,.flickr_badge_image a,.blog-post h2 a,.blog-img a,.nav-tabs a,.article-img  a,#links a)"));
	
	/* Add ".no-flip" class to "a" tag or "ul" tag to remove flip effect*/ 
	
	
	/*=================== Submenu click event  Start=======================*/

	$('ul.dropdown-menu [data-toggle=dropdown]').on('click', function(event) { 
	   event.preventDefault();  
	   event.stopPropagation(); 
	   // If a menu is already open we close it
	 	  //$('ul.dropdown-menu [data-toggle=dropdown]').parent().removeClass('open');
	   // opening the one you clicked on
	   $(this).parent().addClass('open');
	
	   var menu = $(this).parent().find("ul");
	   var menupos = menu.offset();
	 
	   if ((menupos.left + menu.width()) + 30 > $(window).width()) {
	       var newpos = - menu.width();      
	   } else {
	       var newpos = $(this).parent().width();
	   }
	   menu.css({ left:newpos }); 
	});
	 
	 

	/*======= For Banner carousel on Index Page  =================== */

	$('#myCarousel').carousel({
		interval :3000
	}); 
	$('#testiCarousel').carousel({
		interval : 4000
	});
	$('#projectCarousel').carousel({
		interval : 4000
	});
 
	

	/*=======  For Scroll to top  =================== */
	$('.top-btn').click(function(event) {
		event.preventDefault();
		var liIndex = $(this).index();
		var contentPosTop = $('html').eq(liIndex).position().top;

		$('html, body').stop().animate({
			scrollTop : contentPosTop
		}, 1000);
	});
	
	/* ---------- Start : Portfoilo filter animation--------- */
	
	jQuery.browser={};(function(){jQuery.browser.msie=false;
	jQuery.browser.version=0;if(navigator.userAgent.match(/MSIE ([0-9]+)\./)){
	jQuery.browser.msie=true;jQuery.browser.version=RegExp.$1;}})();
	
	/*Add id to the portfolio thumbnails*/
	var thumbid; 
	var thid = 1;
	$('.portfolio.thumbnails>li').each(function() { 
		thumbid = 'id-'+thid;
		$(this).attr('data-id',thumbid); 
		thid++;
	});
	 
	
	// get the action filter option item on page load
	var $filterType = $('#filtrable li.active a').attr('class'); 
	var $holder = $('ul.thumbnails'); 
	var $data = $holder.clone(); 
	$('#filtrable li a').click(function(e) {	 
		$('#filtrable li').removeClass('active'); 
		var $filterType = $(this).attr('class').split(' ').slice(-1)[0]; 
		$(this).parent().addClass('active');  
		if ($filterType == 'all') { 
			var $filteredData = $data.find('li');
		} else { 
			
			var dataTypeSplit = $data.find('li').attr('data-type').split(' ');   
			$data.find('li[data-type]').each(function() { 
				  for(i=0;i<dataTypeSplit.length;i++){  
				  	 var eleTypeArr =$(this).attr('data-type').split(' '); 
				  	  if ($.inArray( $filterType , eleTypeArr) !== -1)
						{
							  $(this).attr('data-newtype', $filterType); 
						} 
				 }
			});
			 
			var $filteredData = $data.find('li[data-newtype=' + $filterType + ']');
		} 
		// call quicksand and assign transition parameters
		$holder.quicksand($filteredData, {
			duration : 800, 
			easing : 'easeInOutQuad'
		});
		return false;
	});
	
	// Touch device porfolio Animation 
	$(".touch .thumbnail-box").hover(function() {
		$(".touch .thumbnail-box").addClass('portfolio-active');
	}, function() {
		$(".touch .thumbnail-box").removeClass('portfolio-active');
	});
	/* ---------- End : Portfoilo filter animation--------- */
	
	
	
	

});

 $(window).resize(function() {
		setthumbsize();
	});

	function setthumbsize() {
		var thumbHeight = $('ul.thumbnails .item').height(), thumbWidth = $('ul.thumbnails .item').outerWidth();
		$('ul.thumbnails .item').css({
			'max-width' : thumbWidth,
			'max-height' : thumbHeight
		}); 
	}
setthumbsize();


	/*=======For Phone carousel=================== */
 
$(window).load(function() {
        $('#carousel-screen').carousel({
		interval : 3000
		});
        $(".carousel-nav a").click(function(e){
            e.preventDefault();
            var index = parseInt($(this).attr('data-to'));
            $('#carousel-screen').carousel(index);
            var nav = $('.carousel-nav');
            var item = nav.find('a').get(index);
            nav.find('a.active').removeClass('active');
            $(item).addClass('active');
        });

        $("#carousel-screen").bind('slide', function(e) {
          
          var elements = $('#carousel-screen').attr('data-sliderCount');
          var nav = $('.carousel-nav');
          var index = $('#carousel-screen').find('.item.active').index();
          index = (index == elements - 1) ? 0 : index + 1;
          var item = nav.find('a').get(index);
          nav.find('a.active').removeClass('active');
          $(item).addClass('active');
        });
  });
 

