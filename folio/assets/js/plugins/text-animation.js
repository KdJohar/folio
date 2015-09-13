$("document").ready(function(){ 
		function reaplayanimation(interval){
			var aniInterval = window.setInterval(replay,interval+5000);
			function replay(){
				 $(".animateme").height($(".animateme").outerHeight()); 
				 $(".letter").fadeOut(1000).delay(1000).fadeIn();
			}
		}
		var supports3DTransforms = document.body.style['webkitPerspective'] !== undefined || document.body.style['MozPerspective'] !== undefined;
		
		function anify(selector,char_crossfade) { 
			var cc = (char_crossfade!=null)?char_crossfade:"150"; 
			var ad=0;
			var repeat_ani;
			
			if (supports3DTransforms) {  
				$.each(selector, function() { 
					var nodes = $(this);
					var char_count=$.trim( nodes.text()).length;
					repeat_ani  = char_count *char_crossfade;
					
					var char_at=$.trim( nodes.text()); 
					nodes.empty();
					for(var i=0;i<char_count;i++ ){ 
						var node = char_at[i];
						if (node!=" "){
							nodes.append('<span  class="letter"  data-letter="' + node + '">' + 
							'<span class="char2" style="-webkit-animation-delay:' + ((i*cc)+ad) + 
							'ms;-moz-animation-delay:' + ((i*cc)+ad) + 'ms;'+
							'ms;-ms-animation-delay:' + ((i*cc)+ad) + 'ms;'+
							'ms;-o-animation-delay:' + ((i*cc)+ad) + 'ms;'+
							'ms;animation-delay:' + ((i*cc)+ad) + 'ms;" >'+
							node+'</span>'+ 
							node +  
							'<span class="char1" style="-webkit-animation-delay:' + ((i*cc)+ad) + 
							'ms;-moz-animation-delay:' + ((i*cc)+ad) + 'ms;'+
							'ms;-ms-animation-delay:' + ((i*cc)+ad) + 'ms;'+
							'ms;-o-animation-delay:' + ((i*cc)+ad) + 'ms;'+
							'ms;animation-delay:' + ((i*cc)+ad) + 'ms;" >'+
							node+'</span>'+ 
							'</span>'); 
						}else{
							nodes.append('<span class="letter"> &nbsp </span>');
						} 
					}
					ad+=(char_count*char_crossfade);
				});  
			}else{
				selector.addClass("letter");
			}
			
			reaplayanimation(repeat_ani);
			 
		} 
		
		//Add class name here followed by crossfade charactor animation delay in millisecond
		var txt=$("#animatedTxt").text();
		$("#animatedTxt").text('');
		$("#animatedTxt").css('opacity','1');
	    var txtrow = txt.split('#'); 
		
		for(i=0;i<txtrow.length;i++){ 
 			var txtword = txtrow[i].replace("_", " ");
 			$("#animatedTxt").append('<div class="animateme">'+txtword+'</div>');
		}
		//Add class name here followed by crossfade charactor animation delay in millisecond
		anify($(".animateme"),200);  
	}); 