from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    """
    Display the list of all contacts.
    This is the main view that shows all contact cards.
    """
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_create(request):
    """
    Handle contact creation.
    - GET: Display the contact creation form
    - POST: Process the form submission
        - If HTMX request: Return just the new contact card
        - If regular request: Redirect to contact list
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            if request.headers.get('HX-Request'):
                # For HTMX requests, return just the new contact card
                return HttpResponse(
                    render_to_string('contacts/partials/contact_card.html', 
                                   {'contact': contact}),
                    headers={'HX-Trigger': 'contactListChanged'}
                )
            return redirect('contact_list')
    else:
        form = ContactForm()
    
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_edit(request, pk):
    """
    Handle contact editing.
    - GET: Display the contact edit form pre-filled with contact data
    - POST: Process the form submission
        - If HTMX request: Return just the updated contact card
        - If regular request: Redirect to contact list
    """
    # Get the contact or return 404 if not found
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            if request.headers.get('HX-Request'):
                # For HTMX requests, return just the updated contact card
                return HttpResponse(
                    render_to_string('contacts/partials/contact_card.html', 
                                   {'contact': contact}),
                    headers={'HX-Trigger': 'contactListChanged'}
                )
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'contacts/contact_form.html', {'form': form, 'contact': contact})

def contact_delete(request, pk):
    """
    Handle contact deletion.
    - GET: Display the delete confirmation dialog
    - POST: Process the deletion
        - If HTMX request: Return empty response (card will be removed)
        - If regular request: Redirect to contact list
    """
    # Get the contact or return 404 if not found
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        contact.delete()
        if request.headers.get('HX-Request'):
            # For HTMX requests, return empty response with success status
            response = HttpResponse('', status=204)
            response['HX-Trigger'] = 'contactListChanged'
            return response
        return redirect('contact_list')
    
    # For GET requests, return the confirmation dialog
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})
