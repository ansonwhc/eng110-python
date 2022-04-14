from PostcodeService.postcode_service.postcode_manager import PostcodeManager


def postcode(postcode_string):
    return PostcodeManager(postcode_string).get_postcode()


if __name__ == "__main__":
    # example
    pc = postcode("B7 4BB")
    print(pc.admin_district)
