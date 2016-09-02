class MyCookieMiddleware(object):
    """
    This is a middle ware to change view request and reponse to add cookie to the request
    """

    def process_request(self, request):
        """
        This is used to modify requst comming from user
        """
	# Will only add if requested does not have it already
	if not request.COOKIES.get('mycookie'):
	    request.COOKIES['mycookie'] = "cookie1"

    def process_response(self, request, response):
        """
        This is used to modify response
        """
        # Your desired cookie will available in every http responnse parser like browser not in django views
	if not request.COOKIES.get('mycookie'):
	    response.set_cookie("mycookie", "cookie1")
	return response

