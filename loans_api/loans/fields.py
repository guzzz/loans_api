class CurrentIpAddress:
    # def set_context(self, serializer_field):
    #     request = serializer_field.context["request"]
    #     x_forwarded_for = request.META.get("X-Forwarded-For")
    #     if x_forwarded_for:
    #         request_ip = x_forwarded_for.split(",")[0]
    #     else:
    #         request_ip = request.META.get("REMOTE_ADDR")
    #     self.ip_address = request_ip

    def set_context(self, serializer_field):
        request = serializer_field.context["request"]
        self.ip_address = request.META.get("REMOTE_ADDR")

    def __call__(self):
        return self.ip_address


class CurrentUser:
    def set_context(self, serializer_field):
        self.user = serializer_field.context["request"].user

    def __call__(self):
        return self.user
