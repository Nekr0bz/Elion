(function() {

    var app = {

        initialize : function () {
            this.setUpListeners();
        },

        setUpListeners: function () {
            $('.showReply').on('click', app.showReply);
        },

        showReply: function (e) {
            e.preventDefault();
            $('.show').addClass('hide').removeClass('show')

            var obj_id = $(this).attr('id'),
                reply = $('div[id='+obj_id+']');

            $(reply).removeClass('hide').addClass('show');
            $(reply).find('textarea').attr('placeholder', 'Ответить на отзыв клиента');
            $(reply).find('button.submit').html('Ответить').attr('id','showReply');
            $(reply).find('button.cancel').attr('id','showReply');
        }
        
    };

    app.initialize();

}());
