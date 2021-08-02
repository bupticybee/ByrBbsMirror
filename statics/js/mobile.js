var forms = $("form").last()
forms.parent().before('<form id="form_reply" action="" method="post"><textarea id="reply_txt" name="content" style="width:100%" rows="1"></textarea><br><input id="but_reply" type="submit" class="btn" value="快速回复"><input type="hidden" name="subject" value=""></form>')
forms.parent().after('<form action="http://search.icybee.cn/bbs" method="get"><span class="f">全站搜索</span><br /><input type="text" name="key" />&nbsp;<input type="submit" value="GO" class="btn" /><a href="http://job.icybee.cn"><h4>论坛招聘信息</h4></a>回帖已经开发完成，各位如果有需要的功能有反馈发到icybee@yeah.net')

btn= $('#but_reply')
txt = $('#reply_txt')
frm = $('#form_reply')

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
                        var nice = $("li").first().next()
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
                alert('success!')
                location.reload();
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log('error')
                alert('committed!')
                location.reload();
            }
        });
})
$('.sp').css('position','relative')
$('.like').css('bottom','2px')
$('img').css('max-width','100%')
