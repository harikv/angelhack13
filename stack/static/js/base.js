$(function(){

$('#loading_modal').bind('show', function() {
		//add custom message to loading modal window
		//call $('#loading_modal').data('loading_message', 'Your message...').modal('show');
    	var loading_message = $(this).data('loading_message');
		if(typeof loading_message !== "undefined")
		{
			$(this).find("#myModalLabel").text(loading_message);
		}
		
});


});

function DisableButton(b)
{
      b.disabled = true;
      b.value = 'Submitting';
      b.form.submit();
}