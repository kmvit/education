$(document).ready(function(){
	var banner = $('#banner').height();
	banner = banner + 60;
	$('#listNews').css('height', banner-101 + 'px');

$( function() {
    $( "#slider-range" ).slider({
      range: true,
      min: 0,
      max: 500,
      values: [ 75, 300 ],
      slide: function( event, ui ) {
        $( "#selectPrice" ).val( ui.values[ 0 ] );
        $( "#selectPrice2" ).val( ui.values[ 1 ] );
      }
    });
    $( "#selectPrice" ).val( $( "#slider-range" ).slider( "values", 0 ));

    $( "#selectPrice2" ).val( $( "#slider-range" ).slider( "values", 1 ) );
  } );
});