RULES = [
    ('api/v2/services', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/services', 'list', 'admin', '*', '*', '*'),
    ('api/v2/services', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/services', 'list', 'observer', '*', '*', '*'),
    ('api/v2/services', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/services', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/services', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/services', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/services', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/services', 'create', 'admin', '*', '*', '*'),
    ('api/v2/services', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/services', 'update', 'admin', '*', '*', '*'),
    ('api/v2/services', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/services', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/service-trls', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/service-trls', 'list', 'admin', '*', '*', '*'),
    ('api/v2/service-trls', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-trls', 'list', 'observer', '*', '*', '*'),
    ('api/v2/service-trls', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/service-trls', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/service-trls', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-trls', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/service-trls', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/service-trls', 'create', 'admin', '*', '*', '*'),
    ('api/v2/service-trls', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/service-trls', 'update', 'admin', '*', '*', '*'),
    ('api/v2/service-trls', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/service-trls', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/service-areas', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/service-areas', 'list', 'admin', '*', '*', '*'),
    ('api/v2/service-areas', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-areas', 'list', 'observer', '*', '*', '*'),
    ('api/v2/service-areas', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/service-areas', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/service-areas', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-areas', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/service-areas', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/service-areas', 'create', 'admin', '*', '*', '*'),
    ('api/v2/service-areas', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/service-areas', 'update', 'admin', '*', '*', '*'),
    ('api/v2/service-areas', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/service-areas', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/institutions', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/institutions', 'list', 'admin', '*', '*', '*'),
    ('api/v2/institutions', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/institutions', 'list', 'observer', '*', '*', '*'),
    ('api/v2/institutions', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/institutions', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/institutions', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/institutions', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/institutions', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/institutions', 'create', 'admin', '*', '*', '*'),
    ('api/v2/institutions', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/institutions', 'update', 'admin', '*', '*', '*'),
    ('api/v2/institutions', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/institutions', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/user-roles', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/user-roles', 'list', 'admin', '*', '*', '*'),
    ('api/v2/user-roles', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/user-roles', 'list', 'observer', '*', '*', '*'),
    ('api/v2/user-roles', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/user-roles', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/user-roles', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/user-roles', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/user-roles', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/user-roles', 'create', 'admin', '*', '*', '*'),
    ('api/v2/user-roles', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/user-roles', 'update', 'admin', '*', '*', '*'),
    ('api/v2/user-roles', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/user-roles', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/user-customers', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/user-customers', 'list', 'admin', '*', '*', '*'),
    ('api/v2/user-customers', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/user-customers', 'list', 'observer', '*', '*', '*'),
    ('api/v2/user-customers', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/user-customers', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/user-customers', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/user-customers', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/user-customers', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/user-customers', 'create', 'admin', '*', '*', '*'),
    ('api/v2/user-customers', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/user-customers', 'update', 'admin', '*', '*', '*'),
    ('api/v2/user-customers', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/user-customers', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/custom-users', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/custom-users', 'list', 'admin', '*', '*', '*'),
    ('api/v2/custom-users', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/custom-users', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/custom-users', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/custom-users', 'create', 'admin', '*', '*', '*'),
    ('api/v2/custom-users', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/custom-users', 'update', 'admin', '*', '*', '*'),
    ('api/v2/custom-users', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/custom-users', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/service-owners', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/service-owners', 'list', 'admin', '*', '*', '*'),
    ('api/v2/service-owners', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-owners', 'list', 'observer', '*', '*', '*'),
    ('api/v2/service-owners', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/service-owners', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/service-owners', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-owners', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/service-owners', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/service-owners', 'create', 'admin', '*', '*', '*'),
    ('api/v2/service-owners', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/service-owners', 'update', 'admin', '*', '*', '*'),
    ('api/v2/service-owners', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/service-owners', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/contact-information', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/contact-information', 'list', 'admin', '*', '*', '*'),
    ('api/v2/contact-information', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/contact-information', 'list', 'observer', '*', '*', '*'),
    ('api/v2/contact-information', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/contact-information', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/contact-information', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/contact-information', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/contact-information', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/contact-information', 'create', 'admin', '*', '*', '*'),
    ('api/v2/contact-information', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/contact-information', 'update', 'admin', '*', '*', '*'),
    ('api/v2/contact-information', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/contact-information', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/contact_information_internal', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'list', 'admin', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'list', 'observer', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'create', 'admin', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'update', 'admin', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/contact_information_internal', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/users', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/users', 'list', 'admin', '*', '*', '*'),
    ('api/v2/users', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/users', 'list', 'observer', '*', '*', '*'),
    ('api/v2/users', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/users', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/users', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/users', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/users', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/users', 'create', 'admin', '*', '*', '*'),
    ('api/v2/users', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/users', 'update', 'admin', '*', '*', '*'),
    ('api/v2/users', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/users', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/service-versions', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/service-versions', 'list', 'admin', '*', '*', '*'),
    ('api/v2/service-versions', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-versions', 'list', 'observer', '*', '*', '*'),
    ('api/v2/service-versions', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/service-versions', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/service-versions', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-versions', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/service-versions', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/service-versions', 'create', 'admin', '*', '*', '*'),
    ('api/v2/service-versions', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/service-versions', 'update', 'admin', '*', '*', '*'),
    ('api/v2/service-versions', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/service-versions', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/service-status', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/service-status', 'list', 'admin', '*', '*', '*'),
    ('api/v2/service-status', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-status', 'list', 'observer', '*', '*', '*'),
    ('api/v2/service-status', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/service-status', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/service-status', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/service-status', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/service-status', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/service-status', 'create', 'admin', '*', '*', '*'),
    ('api/v2/service-status', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/service-status', 'update', 'admin', '*', '*', '*'),
    ('api/v2/service-status', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/service-status', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/components', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/components', 'list', 'admin', '*', '*', '*'),
    ('api/v2/components', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/components', 'list', 'observer', '*', '*', '*'),
    ('api/v2/components', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/components', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/components', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/components', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/components', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/components', 'create', 'admin', '*', '*', '*'),
    ('api/v2/components', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/components', 'update', 'admin', '*', '*', '*'),
    ('api/v2/components', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/components', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/component-implementations', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementations', 'list', 'admin', '*', '*', '*'),
    ('api/v2/component-implementations', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/component-implementations', 'list', 'observer', '*', '*', '*'),
    ('api/v2/component-implementations', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementations', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/component-implementations', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/component-implementations', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/component-implementations', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementations', 'create', 'admin', '*', '*', '*'),
    ('api/v2/component-implementations', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementations', 'update', 'admin', '*', '*', '*'),
    ('api/v2/component-implementations', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementations', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/component-implementation-details', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'list', 'admin', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'list', 'observer', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'create', 'admin', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'update', 'admin', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-details', 'delete', 'superadmin', '*', '*', '*'),

    ('api/v2/component-implementation-detail-links', 'list', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'list', 'admin', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'list', 'serviceowner', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'list', 'observer', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'retrieve', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'retrieve', 'admin', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'retrieve', 'serviceowner', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'retrieve', 'observer', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'create', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'create', 'admin', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'update', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'update', 'admin', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'destroy', 'superadmin', '*', '*', '*'),
    ('api/v2/component-implementation-detail-links', 'delete', 'superadmin', '*', '*', '*')
]
