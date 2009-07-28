$(document).ready(function(){
    // if some images already availible fire jqueryUI sortables
    $("div.image_container").sortable({
      stop: function(e,ui) {
      ui.item.css({'top':'0','left':'0'});
      }
      });
    //$("div.image_container").sortable({ containment: 'parent', appendTo: 'body' });
    // event binding
    $("div.image_block").hover(show_buttons, hide_buttons); // eof image_block hover
    $("a.delete_image").bind("click.delete_image",confirm_remove_image); // eof a.delete (...) .click

    // image uploading
    $("iframe.image_upload_form").load(function(){
      $("div.uploading").remove(); // hide progressbar
      // auto resize the iframe
      this.style.height = this.contentWindow.document.body.offsetHeight + 'px';
      $("iframe.image_upload_form").contents().find("input[type='submit']").click(function(){
        $("div.iframe_container").prepend('<div class="uploading"></div>');
        //if($("div.image_block").length == 1){ $("div.image_container").sortable(); }
        }); // eof iframe submit click
      frame_callback = $("iframe.image_upload_form").contents().find("input#callback").val();
      if(frame_callback != 0) {
      var data = $.secureEvalJSON(frame_callback); // convert json to object securely
      var new_image = $('<div class="image_block"><span class="image_id">'+data['id']+'</span><a href="/admin/imaging/image/'+data['id']+'/" class="edit_image">Edit</a><a href="#" class="delete_image">Delete</a><img src="'+data['image']+'" alt="'+data['alt']+'" /><span class="image_name">'+data['name']+'</span></div>');
      $("div.image_container").append(new_image); // add new image to the list
      $("div.image_container").sortable("refresh"); // make it sortable
      $("a.delete_image").unbind("click.delete_image").bind("click.delete_image",confirm_remove_image); // rebind click event
      $("div.image_block").hover(show_buttons, hide_buttons); // rebind hover events

      } // eof frame_callback handling
      }); // eof $("iframe.image (...).load(...

    $("div#content-main > form").submit(function(){
        var images_ids = ''; 
        $("div.image_block").each(function(i){
          var image_id = $(this).find("span.image_id").text();
          if(i == 0) { images_ids += image_id; } else { images_ids += ","+image_id; }
          }); // eof .each
        $("input.imaging_data").val(images_ids);
        }); // eof .submit

    }); // eof doc ready ============================================================

// helper functions:

function confirm_remove_image(){
  $(".remove_confirm").remove();
  var dialog_box = '<div class="remove_confirm">Are you sure? <br /> <input type="button" name="yes" value="Yes" /> <input type="button" name="no" value="No" /> </div>';
  var image_block = $(this).parent();
  image_block.append(dialog_box);
  $("input[name='yes']").bind('click.removal',remove_image);
  $("input[name='no']").bind('click.removal', function(){image_block.find(".remove_confirm").remove();});
  return false;
}

function remove_image(){
  var image_block = $(this).parent().parent();
  var id = image_block.find("span.image_id").text();
  $.post('/imaging/ajax_delete/', {'id':id}, function(data){
      if(data == 'ok') {
      image_block.fadeOut('slow', function(){ image_block.remove(); }); 
      }
      }, "text");
}

function show_buttons(){
  $(this).find("a.edit_image, a.delete_image").css("top", "4px");
}

function hide_buttons(){
  $(this).find("a.edit_image, a.delete_image").css("top", "-9999em");
}
