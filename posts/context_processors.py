def categories(request):
    categories = ['Programming',
                  'Travel',
                  'Food'
                  ]
    
    return {'categories':categories}