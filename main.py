
from ticket_service import TicketService
from ticket_type_request import TicketTypeRequest


if __name__ == '__main__':

    ticket_service = TicketService()

    #this is included for the demo purpose and you can change the demo values here
    r1 = TicketTypeRequest("ADULT", 10)
    r2 = TicketTypeRequest("ADULT", 2)
    r3 = TicketTypeRequest("INFANT", 12)
    list1 = [r1,r2,r3]

    ticket_service.purchase_tickets(1,list1)

