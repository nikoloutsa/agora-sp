.meta:
  root_url: https://snf-789670.vm.okeanos.grnet.gr
  get_rules: agora.utils.get_rules
  djoser_verifier: agora.utils.djoser_verifier
  userid_extractor: agora.utils.userid_extractor
api/v2:
  .endpoint: {}
  users:
    .collection:
      model: accounts.models.User
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      username:
        .string: {}
      email:
        .string: {}
      first_name:
        .string: {}
      last_name:
        .string: {}
      is_staff:
        .boolean: {}
      is_active:
        .boolean: {}
      date_joined:
        .string: {}
      avatar:
        .file: {}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  services:
    .collection:
      model: service.models.Service
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
        .filterable: {}
        .sortable: {}
      short_description:
        .string: {}
        .nullable: {}
      description_external:
        .string: {}
        .nullable: {}
      description_internal:
        .string: {}
        .nullable: {}
      service_area:
        .ref:
          to: /api/v2/service-areas
        .nullable: {}
        .sortable: {}
        .filterable: {}
      service_type:
        .string: {}
        .nullable: {}
        .filterable: {}
      service_trl:
        .ref:
          to: /api/v2/service-trls
        .sortable: {}
        .filterable: {}
        .nullable: {}
      request_procedures:
        .string: {}
        .nullable: {}
      funders_for_service:
        .string: {}
        .nullable: {}
      value_to_customer:
        .string: {}
        .nullable: {}
      risks:
        .string: {}
        .nullable: {}
      competitors:
        .string: {}
        .nullable: {}
      id_contact_information:
        .nullable: {}
        .ref:
          to: /api/v2/contact-information
      id_contact_information_internal:
        .nullable: {}
        .ref:
          to: /api/v2/contact-information
      logo:
        .file: {}
      service_owners_ids:
        .string: {}
        .readonly: {}
      .actions=:
        .retrieve: {}
        .delete: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  service-versions:
    .collection:
      model: service.models.ServiceDetails
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service:
        .filterable: {}
        .ref:
          to: /api/v2/services
      status:
        .filterable: {}
        .nullable: {}
        .ref:
          to: /api/v2/service-status
      version:
        .string: {}
      features_current:
        .string: {}
        .nullable: {}
      features_future:
        .string: {}
        .nullable: {}
      usage_policy_has:
        .boolean: {}
      usage_policy_url:
        .string: {}
        .nullable: {}
      privacy_policy_has:
        .boolean: {}
      privacy_policy_url:
        .string: {}
        .nullable: {}
      user_documentation_has:
        .boolean: {}
      user_documentation_url:
        .blankable: {}
        .nullable: {}
        .string: {}
      operations_documentation_has:
        .boolean: {}
      operations_documentation_url:
        .string: {}
        .nullable: {}
      monitoring_has:
        .boolean: {}
      monitoring_url:
        .string: {}
        .nullable: {}
      accounting_has:
        .boolean: {}
      accounting_url:
        .string: {}
        .nullable: {}
      business_continuity_plan_has:
        .boolean: {}
      business_continuity_plan_url:
        .string: {}
        .nullable: {}
      disaster_recovery_plan_has:
        .boolean: {}
      disaster_recovery_plan_url:
        .string: {}
        .nullable: {}
      decommissioning_procedure_has:
        .boolean: {}
      decommissioning_procedure_url:
        .string: {}
        .nullable: {}
      cost_to_run:
        .string: {}
        .nullable: {}
      cost_to_build:
        .string: {}
        .nullable: {}
      use_cases:
        .string: {}
        .nullable: {}
      is_in_catalogue:
        .boolean: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  user-customers:
    .collection:
      model: service.models.UserCustomer
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .ref:
          to: api/v2/user-roles
      role:
        .string: {}
        .nullable: {}
      service_id:
        .ref:
          to: api/v2/services
      .actions=:
        .retrieve: {}
        .delete: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  service_dependsOn_services:
    .collection:
      model: service.models.Service_DependsOn_Service
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service_one:
        .ref: {'to': '/api/v2/service'}
      id_service_two:
        .ref: {'to': '/api/v2/service'}
  service_externalServices:
    .collection:
      model: service.models.Service_ExternalService
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service:
        .ref: {'to': '/api/v2/service'}
      id_external_service:
        .ref: {'to': '/api/v2/external_service'}
  service-status:
    .collection:
      model: service.models.ServiceStatus
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      value:
        .string: {}
        .sortable: {}
        .filterable: {}
      order:
        .integer: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  service-trls:
    .collection:
      model: service.models.ServiceTrl
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      value:
        .string: {}
        .filterable: {}
        .sortable: {}
      order:
        .integer: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  external_services:
    .collection:
      model: service.models.ExternalService
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      description:
        .string: {}
      service:
        .string: {}
      details:
        .string: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  user-roles:
    .collection:
      model: service.models.UserRole
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  user_customers:
    .collection:
      model: service.models.UserCustomer
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .ref: {'to': '/api/v2/user_role'}
      service_id:
        .ref: {'to': '/api/v2/service'}
      role:
        .string: {}
  service-areas:
    .collection:
      model: service.models.ServiceArea
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      icon:
        .file: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  service-owners:
    .collection:
      model: service.models.ServiceOwnership
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      owner: 
        .ref:
          to: /api/v2/custom-users
        .filterable: {}
      service:
        .ref:
          to: /api/v2/services
        .filterable: {}
      state:
        .string: {}
        .filterable: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  custom-users:
    .collection:
      model: accounts.models.User
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      username:
        .string: {}
      email:
        .string: {}
      first_name:
        .string: {}
        .nullable: {}
      last_name:
        .string: {}
        .nullable: {}
      is_staff:
        .boolean: {}
      is_active:
        .boolean: {}
      date_joined:
        .datetime: {}
      avatar:
        .file: {}
      shibboleth_id:
        .string: {}
        .readonly: {}
        .nullable: {}
      role:
        .string: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  contact-information:
    .collection:
      model: owner.models.ContactInformation
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      first_name:
        .string: {}
        .nullable: {}
      last_name:
        .string: {}
        .nullable: {}
      email:
        .string: {}
        .nullable: {}
      phone:
        .string: {}
        .nullable: {}
      url:
        .string: {}
        .nullable: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  institutions:
    .collection:
      model: owner.models.Institution
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
        .nullable: {}
      address:
        .string: {}
        .nullable: {}
      country:
        .string: {}
        .nullable: {}
      department:
        .string: {}
        .nullable: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  components:
    .collection:
      model: component.models.ServiceComponent
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
        .nullable: {}
      description:
        .string: {}
        .nullable: {}
      logo:
        .file: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  component-implementations:
    .collection:
      model: component.models.ServiceComponentImplementation
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      component_id:
        .filterable: {}
        .ref: {'to': '/api/v2/components'}
      name:
        .string: {}
        .nullable: {}
      description:
        .string: {}
        .nullable: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  component-implementation-details:
    .collection:
      model: component.models.ServiceComponentImplementationDetail
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      component_id:
        .filterable: {}
        .ref: {'to': '/api/v2/components'}
      component_implementation_id:
        .filterable: {}
        .ref: {'to': '/api/v2/component-implementations'}
      version:
        .string: {}
        .nullable: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  component-implementation-detail-links:
    .collection:
      model: component.models.ServiceDetailsComponent
    .protected=:
      .djoser: {}
    '*':
      id:
        .uuid: {}
        .readonly: {}
      service_id:
        .filterable: {}
        .ref: {'to': '/api/v2/services'}
      service_details_id:
        .filterable: {}
        .ref: {'to': '/api/v2/service-versions'}
      service_component_implementation_detail_id:
        .filterable: {}
        .ref: {'to': '/api/v2/component-implementation-details'}
      configuration_parameters:
        .string: {}
        .nullable: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
