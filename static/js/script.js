$(document).ready(function(){
    $('.collapsible').collapsible();
    $('.sidenav').sidenav();
    $('.delete_confirm').hide();
    $('.delete').click(function(){
      $('.delete_confirm').toggle();
    });
    $('.delete_confirm').click(function(){
      $('.delete_confirm').hide();
    });
  });

