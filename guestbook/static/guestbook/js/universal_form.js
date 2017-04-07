(function() {

    var app = {

        initialize : function () {
            this.setUpListeners();
        },

        setUpListeners: function () {
            $('.showReply').on('click', app.showReply);
            $('a.changeReview').on('click', app.showChangeReview);
            $('a.changeReply').on('click', app.changeReply);
        },

        showReply: function (e) {
            e.preventDefault();
            app.prevChanges();

            var obj_id = $(this).attr('id'),
                reply = $('div[id='+obj_id+']');

            $(reply).find('textarea').attr('placeholder', 'Ответить на отзыв клиента');
            $(reply).find('button.submit').html('Ответить').attr('id','showReply');
            $(reply).find('button.cancel').attr('id','showReply');

            $(reply).removeClass('hide').addClass('show');
        },

        showChangeReview: function () {
            app.prevChanges();

            var obj_id = $(this).attr('id'),
                new_review = $('div[id='+obj_id+']'),
                this_review = $(this).parents('div.quote-box'),
                obj_text = $(this_review).find('p').html();

            $(this_review).addClass('hide');
            $(new_review).find('textarea').html(obj_text);
            $(new_review).find('button.submit').html('Сохранить').attr('id','showChangeReview');
            $(new_review).find('button.cancel').attr('id','showChangeReview');

            $(new_review).removeClass('hide').addClass('show');
        },

        changeReply: function () {
            app.prevChanges();

            var obj_id = $(this).attr('id'),
                new_reply = $('div[id='+obj_id+']'),
                this_reply = $(this).parents('div.author-box'),
                obj_text = $(this_reply).find('p').html();

            $(this_reply).addClass('hide');
            $(new_reply).find('textarea').html(obj_text).attr('placeholder', 'Ответить на отзыв клиента');
            $(new_reply).find('button.submit').html('Сохранить').attr('id','changeReply');
            $(new_reply).find('button.cancel').attr('id','changeReply');

            $(new_reply).removeClass('hide').addClass('show');
        },

        prevChanges: function () {
            $('div.form_universal.show').addClass('hide').removeClass('show');
            $('div.quote-box.hide').removeClass('hide');
            $('div.author-box.hide').removeClass('hide');
        }

    };

    app.initialize();

}());
