    def computeDifference(self):
        max_dif = 0
        for x in range(0, len(self.__elements)):
            for i in range(x, len(self.__elements)):
                if x!=i:
                    dif = abs(self.__elements[x] - self.__elements[i])
                    max_dif = max(dif, max_dif)
        self.maximumDifference = int(max_dif)
            