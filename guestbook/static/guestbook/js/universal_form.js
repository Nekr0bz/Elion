(function() {

    var app = {

        initialize : function () {
            this.setUpListeners();
        },

        setUpListeners: function () {
            $('.showReply').on('click', app.showReply);
            $('a.changeReview').on('click', app.showChangeReview);
            $('a.changeReply').on('click', app.showChangeReply);
            $('button.cancel').on('click', app.hideUniversalForm);
            $('a[data-action-del]').on('click', app.deleteObject);
            $('button.btn-review.submit').on('click', app.routeActions);
        },

        getCookie: function(name){
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);

                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },

        showReply: function (e) {
            e.preventDefault();
            app.returnChanges(e);

            var obj_id = $(this).attr('data-objid'),
                reply = $('div[id='+obj_id+']');

            $(reply).find('textarea').attr('placeholder', 'Ответить на отзыв клиента');
            $(reply).find('button.submit').html('Ответить').attr('id','showReply');
            $(reply).find('form').attr('action','/guestbook/reply/'+obj_id+'/');

            $(reply).removeClass('hide').addClass('show');
        },

        showChangeReview: function (e) {
            e.preventDefault();
            app.returnChanges(e);

            var obj_id = $(this).attr('data-objid'),
                new_review = $('div[id='+obj_id+']'),
                this_review = $(this).parents('div.quote-box'),
                obj_text = $(this_review).find('p').html();

            $(this_review).addClass('hide');
            $(new_review).find('textarea').html(obj_text);
            $(new_review).find('button.submit').html('Сохранить').attr('id','showChangeReview').attr('data-action-upd','');
            $(new_review).find('form').attr('action','/guestbook/update/'+obj_id+'/').attr('data-target-upd', obj_id);;

            $(new_review).removeClass('hide').addClass('show');
        },

        showChangeReply: function (e) {
            e.preventDefault();
            app.returnChanges(e);

            var obj_id = $(this).attr('data-objid'),
                new_reply = $('div[id='+obj_id+']'),
                parent_id = $(new_reply).attr('data-parentid'),
                this_reply = $(this).parents('div.author-box'),
                obj_text = $(this_reply).find('p').html();

            $(this_reply).addClass('hide');
            $(new_reply).find('textarea').html(obj_text).attr('placeholder', 'Ответить на отзыв клиента');
            $(new_reply).find('button.submit').html('Сохранить').attr('id','showChangeReply').attr('data-action-upd','');
            $(new_reply).find('form').attr('action','/guestbook/update/'+parent_id+'/').attr('data-target-upd', parent_id);

            $(new_reply).removeClass('hide').addClass('show');
        },

        hideUniversalForm: function (e) {
            e.preventDefault();
            app.returnChanges();
        },

        returnChanges: function () {
            $('div.form_universal.show').addClass('hide').removeClass('show');
            $('div.quote-box.hide').removeClass('hide');
            $('div.author-box.hide').removeClass('hide');
            $('button[data-action-upd]').removeAttr('data-action-upd');
        },

        deleteObject: function (e) {
            e.preventDefault();
            $(this).addClass('disabled');
            var parent_div = $(this).parents('div')[1];

            $.ajax({
                url: $(this).attr('href'),
                type: 'POST',
                data: {csrfmiddlewaretoken: app.getCookie('csrftoken')}
            }).done(function (data) {
                if(data['status'] == 'ok'){
                    if ($(parent_div).hasClass('quote-box')){
                        $(parent_div).next('div').remove();
                        if ($(parent_div).next('div').hasClass('author-box')){
                            $(parent_div).next('div').remove();
                        }
                        $(parent_div).next('br').remove();
                        $(parent_div).next('br').remove();
                    }
                    $(parent_div).remove();
                }
                else if (data['stats'] == 'error'){
                    console.log(data)
                }
            });
        },

        routeActions: function (e) {
            if($(this)[0].hasAttribute('data-action-upd')){
                app.removeObject(e, this);
            }
        },

        removeObject: function (e, _this) {
            e.preventDefault();
            $(_this).attr('disabled', '');

            var form = $(_this).parent();

            $.ajax({
                url: form.attr('action'),
                type: 'POST',
                data: form.serialize()
            }).done(function (data) {
                if(data['status'] == 'ok'){
                    var id = $(form).attr('data-target-upd'),
                        text = $(form).find('textarea').val();
                    $('div[data-main-id='+id+']').find('p').html(text);
                    app.returnChanges(e);
                }
                else if (data['stats'] == 'error'){
                    console.log(data);
                }
            }).always(function () {
                $(_this).removeAttr('disabled');
            });
        }
    };

    app.initialize();

}());
