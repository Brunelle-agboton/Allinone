<?php

namespace var\cache\dev\ContainerSsCSRg1;

/**
 * @internal This class has been auto-generated by the Symfony Dependency Injection Component.
 */
class getRedirectControllerService extends App_KernelDevDebugContainer
{
    /**
     * Gets the public 'Symfony\Bundle\FrameworkBundle\Controller\RedirectController' shared service.
     *
     * @return \Symfony\Bundle\FrameworkBundle\Controller\RedirectController
     */
    public static function do($container, $lazyLoad = true)
    {
        include_once \dirname(__DIR__, 4).'/vendor/symfony/framework-bundle/Controller/RedirectController.php';

        $a = ($container->privates['router.request_context'] ?? self::getRouter_RequestContextService($container));

        return $container->services['Symfony\\Bundle\\FrameworkBundle\\Controller\\RedirectController'] = new \Symfony\Bundle\FrameworkBundle\Controller\RedirectController(($container->services['router'] ?? self::getRouterService($container)), $a->getHttpPort(), $a->getHttpsPort());
    }
}
