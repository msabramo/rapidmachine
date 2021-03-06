import t

class l05(t.Test):
    
    class TestResource(t.Resource):

        moved = False
        
        def moved_temporarily(self, req, rsp):
            return self.moved

        def previously_existed(self, req, rsp):
            return True

        def resource_exists(self, req, rsp):
            return False
        
        def to_html(self):
            return "Yay"

    def test_not_moved(self):
        self.TestResource.moved = False
        self.go()
        t.eq(self.rsp.status_code, 410)
        t.eq(self.rsp.response, [])
    
    def test_moved(self):
        self.TestResource.moved = '/foo'
        self.go()
        t.eq(self.rsp.status_code, 307)
        t.eq(self.rsp.location, '/foo')
        t.eq(self.rsp.response, [])
