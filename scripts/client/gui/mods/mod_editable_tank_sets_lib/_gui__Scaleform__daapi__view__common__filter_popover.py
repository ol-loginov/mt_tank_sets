# coding=utf-8
#
#
# Thanks to # https://gitlab.com/xvm/xvm/blob/master/src/xpm/xvm_tankcarousel/filter_popover.py
#

import logging

from gui.Scaleform.daapi.view.common.filter_popover import VehiclesFilterPopover, FILTER_SECTION
from .constants import tank_collection_mapping
from .events import overrideMethod, overrideClassMethod
from .settings import Settings as S

log = logging.getLogger(__name__)

is_comp7_filter_popover = lambda (self): False

try:
    from gui.Scaleform.daapi.view.battle.comp7.filter_popover import Comp7TankCarouselFilterPopover

    log.info("disable VehiclesFilterPopover hooks for Comp7TankCarouselFilterPopover")
    is_comp7_filter_popover = lambda (self): isinstance(self, Comp7TankCarouselFilterPopover)
except:
    log.error("cannot find Comp7TankCarouselFilterPopover")


def enabled_for_self(self):
    if is_comp7_filter_popover(self):
        return False
    return True


@overrideClassMethod(VehiclesFilterPopover, '_generateMapping')
def VehiclesFilterPopover__generateMapping(base, self, *args, **kwargs):
    mapping = base(*args, **kwargs)

    if S.is_mod_enabled():
        mapping[FILTER_SECTION.SPECIALS].extend([tank_collection_mapping(n) for n in S.get_tc_numbers_enabled()])

    return mapping


@overrideMethod(VehiclesFilterPopover, '_getInitialVO')
def _VehiclesFilterPopover_getInitialVO(base, self, *args, **kwargs):
    ret = base(self, *args, **kwargs)

    if S.is_mod_enabled() and enabled_for_self(self):
        special_vo = ret['specials']
        special_mapping = self._VehiclesFilterPopover__mapping[FILTER_SECTION.SPECIALS]

        for n, collection in S.get_enabled_collections():
            filter_index = special_mapping.index(tank_collection_mapping(n))
            filter_vo = special_vo[filter_index]

            tooltip = "{HEADER}%s{/HEADER}" % collection.title
            if collection.tooltip is not None and len(collection.tooltip) > 0:
                tooltip += "{BODY}%s{/BODY}" % collection.tooltip

            filter_vo.update({'value': collection.icon, 'tooltip': tooltip})

    return ret


@overrideMethod(VehiclesFilterPopover, '_getUpdateVO')
def _VehiclesFilterPopover_getUpdateVO(base, self, *args, **kwargs):
    return base(self, *args, **kwargs)


LOADED = True
