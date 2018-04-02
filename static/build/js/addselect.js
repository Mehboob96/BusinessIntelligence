
$(document).ready(function() {

//ASSET ADD
  $(".asset-add-more").click(function(){
      var html = $(".asset-copy-fields").html();
      $(".asset-after-add-more").first().after(html);
  });
//ASSET REMOVE
  $("body").on("click",".remove",function(){
      $(this).parents(".control-group").remove();
  });


//LIABILITY ADD
  $(".liability-add-more").click(function(){
      var html = $(".liability-copy-fields").html();
      $(".liability-after-add-more").first().after(html);
  });
//LIABILITY REMOVE
  $("body").on("click",".remove",function(){
      $(this).parents(".control-group").remove();
  });


//OPERATING ADD
  $(".operating-add-more").click(function(){
      var html = $(".operating-copy-fields").html();
      $(".operating-after-add-more").first().after(html);
  });
//OPERATING REMOVE
  $("body").on("click",".remove",function(){
      $(this).parents(".control-group").remove();
  });


//INVESTING ADD
  $(".investing-add-more").click(function(){
      var html = $(".investing-copy-fields").html();
      $(".investing-after-add-more").first().after(html);
  });
//INVESTING REMOVE
  $("body").on("click",".remove",function(){
      $(this).parents(".control-group").remove();
  });


//FINANCING ADD
  $(".financing-add-more").click(function(){
      var html = $(".financing-copy-fields").html();
      $(".financing-after-add-more").first().after(html);
  });
//FINANCING REMOVE
  $("body").on("click",".remove",function(){
      $(this).parents(".control-group").remove();
  });


//REVENUE ADD
  $(".revenue-add-more").click(function(){
      var html = $(".revenue-copy-fields").html();
      $(".revenue-after-add-more").first().after(html);
  });
//REVENUE REMOVE
  $("body").on("click",".remove",function(){
      $(this).parents(".control-group").remove();
  });


//EXPENSES ADD
  $(".expenses-add-more").click(function(){
      var html = $(".expenses-copy-fields").html();
      $(".expenses-after-add-more").first().after(html);
  });
//EXPENSES REMOVE
  $("body").on("click",".remove",function(){
      $(this).parents(".control-group").remove();
  });

});

//Clone the hidden element and shows it
// $('.add-one').click(function(){
//   $('.new-asset').first().clone().appendTo('.hidden-asset').show();
//   attach_delete();
// });

// $('.add-one').click(function(){
//   $("<div class='col-md-2'></div><div class='col-md-4'><select class='selectpicker' data-live-search='true'><option>Cash</option><option>Equipment</option><option>Inventory</option><option>Accounts Receivable</option></select></div><div class='col-md-1'><p class='delete'>X</p></div>").appendTo(".hidden-asset");
//     attach_delete();
// });


// function attach_delete(){
//   $('.delete').off();
//   $('.delete').click(function(){
//     console.log("click");
//     $(this).closest('.new-asset').first().remove();
//   });
// }
//Attach functionality to delete buttons


//Clone the hidden element and shows it
// $('.add-one').click(function(){
//   $('.dynamic-element').first().clone().appendTo('.dynamic-stuff').show();
//   attach_delete();
// });


//Attach functionality to delete buttons
// function attach_delete(){
//   $('.delete').off();
//   $('.delete').click(function(){
//     console.log("click");
//     $(this).closest('.form-group').remove();
//   });
// }
