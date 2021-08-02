
var section = $("#b_search");
section.keyup(function(){
	if(event.keyCode == 13){
		window.location.href='/go?name=' + section.val();
	}
});

section.parent().parent().after('<li><form method="get" accept-charset="utf-8" action="http://search.icybee.cn/bbs"><span class="x-leaf x-search"><span class="toggler"></span><input charset="utf-8" type="text" name="key" class="input-text" value="Icysearch" id="icy_search"></span></form></li>');

section.parent().parent().before('<li><span class="x-leaf"><span class="toggler"></span><a href="http://job.icybee.cn">Icyjob</a></span></li>');

section.parent().parent().html('<form method="get" accept-charset="utf-8" action="/go"><span class="x-leaf x-search"><span class="toggler"></span><input charset="utf-8" type="text" name="name" class="input-text" value="search section" id="icy_search"></span></form>')

//var notice = $('#notice_nav').html('<a href="mailto:icybee@yeah.net">Hi,it\'s Icybee here, you can find you board by sesarch on the section or entire site on the left side. if you have any suggestion, please send it to icybee@yeah.net </a>')

$.ajaxSetup({
    scriptCharset: "utf-8",
    contentType: "application/json;charset=utf-8"
});

if(!(window.location.href.indexOf("article") <= -1)){
	if(!(window.location.href.indexOf("?") > -1) || (window.location.href.indexOf("?p=1") > -1)){
		var url = window.location.href.replace("?p=1","")
		var articleid = url.split("/")[5]
		var key = $("title").text();
		console.log(key)
		$.ajax({
		    type: "GET",
		    url: "/api/simrecommand",
		    contentType: "application/json; charset=utf-8",
		    dataType: "json",
		    data: {'key':key,'articleid':articleid},
		    success: function(json) {
			console.log('success')
			console.log(json)
			var nice = $(".a-content-wrap").first()
			for(var sim = Math.min(10,json.items.length);sim > 0 ;sim --){
				item = json.items[sim - 1]
				nice.after('<p><a style="font-size:15px" href="' + item.url + '" >' + item.title + '</a></p>')
			}
			nice.after('<br/><br/><h1 style="font-size:30px">' + json.title + '</h1>')
		    },
		    error: function (xhr, textStatus, errorThrown) {
			console.log('error')
		    }
		});
	}
}

// quick post
btn = $('#quick_post div:first input:first')
txt = $('#quick_post div:eq(1) textarea:first')
frm = $('#quick_post')
frm.action = '';
frm.submit(function(){
	return false;
})
btn.click(function(){
	var reply = txt.val();
	var title = 'Re:' + $('title').text();
	var url = window.location.href;
	if(reply == ''){
		return 
	}
	urlsp = url.split('?')
	mainurlsp = urlsp[0].split('/')
	console.log(mainurlsp)
	if(mainurlsp['3'] != 'article'){
		return
	}
	board = mainurlsp[4];
	articleid = mainurlsp[5];
	$.ajax({
	    type: "GET",
	    url: "/api/post_reply",
	    contentType: "application/json; charset=utf-8",
	    //dataType: "json",
	    data: {
		'board':board,
		'articleid':articleid,
		'title':title,
		'reply':reply,
	    },
	    success: function(json) {
		console.log('success')
		alert('success! Maybe have a delay for 10 seconds.')
		location.reload();
	    },
	    error: function (xhr, textStatus, errorThrown) {
		console.log('error')
		alert('committed! Maybe have a delay for 10 seconds')
		location.reload();
	    }
	});
})


$('#ban_ner_wrapper').css("background-image","url(/icyimg/ad_reply.jpg)");
$('#ban_ner_wrapper').css("background-size","contain");



