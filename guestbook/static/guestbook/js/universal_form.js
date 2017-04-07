(function() {

    var app = {

        initialize : function () {
            this.setUpListeners();
        },

        setUpListeners: function () {
            $('.showReply').on('click', app.showReply);
            $('a.changeReview').on('click', app.showChangeReview);
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

        prevChanges: function () {
            $('div.form_universal.show').addClass('hide').removeClass('show');
            $('div.quote-box.hide').removeClass('hide');
        }
        
    };

    app.initialize();

}());
