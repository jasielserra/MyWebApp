from sanitize import sanitize


class AthleteList(list):
    def __init__(self, name,dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    @property
    def top3(self):
         return sorted(set([sanitize(each_t) for each_t  in self]))[0:3]

    @property
    def as_dict(self):
        return ({'Name': self.name,
                        'DOB': self.dob,
                        'Top3': self.top3})
    @property
    def clean_data(self):
        return(sorted(set([sanitize(t) for t in self])))


