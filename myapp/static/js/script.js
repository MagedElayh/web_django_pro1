$(document).ready(function(){
    if($('#result') != null){
        Read();
    }
    $('#create').on('click', function(){
        $firstname = $('#firstname').val();
        $lastname = $('#lastname').val();
 
        if($firstname == "" || $lastname == ""){
            alert("Please complete the required field");
        }else{
            $.ajax({
                url: 'create',
                type: 'POST',
                data: {
                    firstname: $firstname,
                    lastname: $lastname,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    Read();
                    $('#firstname').val('');
                    $('#lastname').val('');
                }
            });
        }
    });
 
    $(document).on('click', '.edit', function(){
        $id = $(this).attr('name');
        window.location = "edit/" + $id;
    });
 
    $('#update').on('click', function(){
        $firstname = $('#firstname').val();
        $lastname = $('#lastname').val();
 
        if($firstname == "" || $lastname == ""){
            alert("Please complete the required field");
        }else{
            $id = $('#member_id').val();
            $.ajax({
                url: 'update/' + $id,
                type: 'POST',
                data: {
                    firstname: $firstname,
                    lastname: $lastname,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    window.location = '/myapp';
                    alert('Updated!');
                }
            });
        }
 
    });
 
    $(document).on('click', '.delete', function(){
        $id = $(this).attr('name');
        $.ajax({
            url: 'delete/' + $id,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                Read();
                alert("Deleted!");
            }
        });
    });


 ///////////////////////////////////////////////////////////////////////////
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
          url: btn.attr("data-url"),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#modal-member .modal-content").html("");
            $("#modal-member").modal("show");
          },
          success: function (data) {
            $("#modal-member .modal-content").html(data.html_form);
          }
        });
      };

    $(".js-create-member").click(loadForm);
 
});
 
function Read(){
    $.ajax({
  url: 'read',
  type: 'POST',
  async: false,
  data:{
   res: 1,
   csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
  },
  success: function(response){
   $('#result').html(response);
  }
    });
}