$(document).ready(function(){

    // табы

    $('.bar-element').on('click',  function() {
      $(this)
        .addClass('bar-element_active').siblings().removeClass('bar-element_active')
        .closest('div.container').find('div.bar-element__content').removeClass('bar-element__content_active').eq($(this).index()).addClass('bar-element__content_active');
    });


  });