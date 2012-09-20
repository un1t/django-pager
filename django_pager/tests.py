import  unittest2
from django_pager.pager import get_page_ranges


class GetPageRangesTest(unittest2.TestCase):


    def test_page1of11(self):
        ranges = get_page_ranges(1, 11)
        self.assertEquals(ranges, [[1,2,3,4,5,6,7,8,9,10,11]])

    def test_page1of200(self):
        ranges = get_page_ranges(1, 11)
        self.assertEquals(ranges, [[1,2,3,4,5,6,7,8,9,10,11]])

    def test_page1of200(self):
        ranges = get_page_ranges(1,200)
        self.assertEquals(ranges, [[1,2,3,4,5,6,7,8], [198,199,200]])

    def test_page57of200(self):
        ranges = get_page_ranges(57, 200)
        self.assertEquals(ranges, [[1,2,3],[55,56,57,58,59],[198,199,200]])

    def test_page194of200(self):
        ranges = get_page_ranges(194, 200)
        self.assertEquals(ranges, [[1,2,3],[192,193,194,195,196],[198,199,200]])

    def test_page200of200(self):
        ranges = get_page_ranges(200, 200)
        self.assertEquals(ranges, [[1,2,3],[193,194,195,196,197,198,199,200]])


if __name__ == '__main__':
    unittest2.main()
