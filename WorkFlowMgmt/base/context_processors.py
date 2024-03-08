

def group_names_processor(request):
    if request.user.is_authenticated:
        group_names = [group.name for group in request.user.groups.all()]
    else:
        group_names = []
    return {'group_names': group_names}
