$(document).ready(function () {
    $('.like').click(function () {
        var target = event.target
        var item_pk = $(target).attr('data-id')

        if (item_pk) {
            $.ajax({
                url: "/like/" + item_pk + "/",
                success: function (data) {
                    if (data.is_like) {
                        var class_heart = "fa fa-thumbs-up"
                    } else {
                        class_heart = "fa fa-thumbs-o-up"
                    }

                    var like_html = '<i class="' + class_heart + '" data-id="' + item_pk + '"></i>'
                    var selector = '#like-' + item_pk

                    $(selector).html(like_html)
                }
            })
        }
    })

    $('.dislike').click(function () {
        var target = event.target
        var item_pk = $(target).attr('data-id')

        if (item_pk) {
            $.ajax({
                url: "/dislike/" + item_pk + "/",
                success: function (data) {
                    if (data.is_dislike) {
                        var class_heart = "fa fa-thumbs-down"
                    } else {
                        class_heart = "fa fa-thumbs-o-down"
                    }

                    var like_html = '<i class="' + class_heart + '" data-id="' + item_pk + '"></i>'
                    var selector = '#dislike-' + item_pk

                    $(selector).html(like_html)
                }
            })
        }
    })
})