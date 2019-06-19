from . import cd_gene

__author__ = 'Yuta A. Takagi'


# this gene is designed for Yuta's model
#
# it is a gene that imparts cellularity on the organism by a function defined in the 'yutas_genome_manager' module
# it evaluates to the same value as the previous gene


class GeneCellularity(cd_gene.Gene):
    def __init__(self, organism):
        super().__init__(organism)
        self.can_be_first_gene = False

    def __repr__(self):
        return 'c_' + str(self.value)

    def execute(self):
        self.value = self.organism.genome[self.organism.genome_read_head - 1].value

    def test_execute(self, food, read_head):
        self.test_value = self.organism.genome[read_head - 1].test_value

    def cost(self):
        return 1

    def fix_pointers(self, index):
        pass
