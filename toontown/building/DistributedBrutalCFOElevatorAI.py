from toontown.building.DistributedCFOElevatorAI import DistributedCFOElevatorAI


class DistributedBrutalCFOElevatorAI(DistributedCFOElevatorAI):
    notify = directNotify.newCategory('DistributedBrutalCFOElevatorAI')

    def sendAvatarsToDestination(self, avIdList):
        if len(avIdList) > 0:
            bossZone = self.bldg.createBossOffice(avIdList, isBrutal=True)
            for avId in avIdList:
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setBossOfficeZoneForce', [bossZone])