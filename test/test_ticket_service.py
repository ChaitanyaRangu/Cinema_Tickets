import unittest
from ticket_service import TicketService
from purchase_exceptions import InvalidPurchaseException
from ticket_type_request import TicketTypeRequest

class TestTicketService(unittest.TestCase):


    def test_validate_total_tickets(self):
        ticket_service = TicketService()
        r1 = TicketTypeRequest("ADULT", 0)
        r2 = TicketTypeRequest("INFANT", 2)
        r3 = TicketTypeRequest("CHILD", 2)
        ticket_service._TicketService__populate_dictionary_with_requests([r1, r2, r3])
        try:
            ticket_service._TicketService__validate_total_tickets()
        except InvalidPurchaseException as e:
            self.assertEqual(type(e), InvalidPurchaseException)
        else:
            self.fail('InvalidPurchaseException not raised')

        r4 = TicketTypeRequest("ADULT",1)
        ticket_service._TicketService__populate_dictionary_with_requests([r4])
        try:
            ticket_service._TicketService__validate_total_tickets()
        except InvalidPurchaseException as e:
            self.assertEqual(type(e), InvalidPurchaseException)
        else:
            self.fail('InvalidPurchaseException not raised')

        r5 = TicketTypeRequest("ADULT", 21)
        ticket_service._TicketService__populate_dictionary_with_requests([r5])
        try:
            ticket_service._TicketService__validate_total_tickets()
        except InvalidPurchaseException as e:
            self.assertEqual(type(e), InvalidPurchaseException)
        else:
            self.fail('InvalidPurchaseException not raised')


    def test_caluculate_total_number_of_seats(self):
        ticket_service1 = TicketService()
        r1 = TicketTypeRequest("ADULT", 10)
        r2 = TicketTypeRequest("INFANT", 2)
        r3 = TicketTypeRequest("CHILD", 2)
        ticket_service1._TicketService__populate_dictionary_with_requests([r1, r2, r3])
        total_seats = ticket_service1._TicketService__caluculate_total_number_of_seats()
        self.assertEqual(total_seats, 12)

    def test_caluculate_total_ammount_to_be_paid(self):
        __ticket_service = TicketService()
        r1 = TicketTypeRequest("ADULT", 10)
        r2 = TicketTypeRequest("INFANT", 2)
        r3 = TicketTypeRequest("CHILD", 2)
        __ticket_service._TicketService__populate_dictionary_with_requests([r1, r2, r3])
        total_ammount = __ticket_service._TicketService__caluculate_total_ammount_to_be_paid()
        self.assertEqual(total_ammount,220)


    def test_populate_dictionary_with_requests(self):
        ticket_service = TicketService()
        r1 = TicketTypeRequest("ADULT", 10)
        r2 = TicketTypeRequest("INFANT", 2)
        r3 = TicketTypeRequest("CHILD", 2)
        ticket_service._TicketService__populate_dictionary_with_requests([r1,r2,r3])
        self.assertEqual(len(ticket_service.type_to_count_dict),3)


    def test_validate_accountid(self):
        ticket_service = TicketService()
        try:
            ticket_service._TicketService__validate_accountid(0)
        except InvalidPurchaseException as e:
            self.assertEqual(type(e), InvalidPurchaseException)
        else:
            self.fail('InvalidPurchaseException not raised')

        try:
            ticket_service._TicketService__validate_accountid("Chaitanya")
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
        else:
            self.fail('TypeError not raised')

    def test_validate_ticket_type_requests(self):
        ticket_service = TicketService()
        try:
            ticket_service._TicketService__validate_ticket_type_requests([])
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
        else:
            self.fail('TypeError not raised')

if __name__ == '__main__':
    unittest.main()