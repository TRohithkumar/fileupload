$(document).on('click' , '#submit', function() {

    var formdata = new FormData(this);

        $.ajax({
            url: "/uploads",
            type: "POST",
            data: formdata,
            mimeTypes:"multipart/form-data",
            contentType: false,
            cache: false,
            processData: false,
            return

         });
    });